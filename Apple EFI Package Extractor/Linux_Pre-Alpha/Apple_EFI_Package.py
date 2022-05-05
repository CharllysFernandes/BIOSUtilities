#!/usr/bin/env python3

"""
Apple EFI Package
Apple EFI Package Extractor
Copyright (C) 2019-2021 Plato Mavropoulos
"""

print('Apple EFI Package Extractor v2.0_Linux_a1')

import os
import sys
import zlib
import shutil
import subprocess

if len(sys.argv) >= 2 :
	pkg = sys.argv[1:]
else :
	pkg = []
	in_path = input('\nEnter the full folder path: ')
	print('\nWorking...')
	for root, dirs, files in os.walk(in_path):
		for name in files :
			pkg.append(os.path.join(root, name))
			
final_path = os.path.join(os.getcwd(), 'AppleEFI')
if os.path.exists(final_path) : shutil.rmtree(final_path)
			
for input_file in pkg :
	file_path = os.path.abspath(input_file)
	file_name = os.path.basename(input_file)
	file_dir = os.path.dirname(file_path)
	file_ext = os.path.splitext(file_path)[1]
	
	print('\nFile: %s\n' % file_name)
	
	with open(input_file, 'rb') as in_buff : file_adler = zlib.adler32(in_buff.read()) & 0xFFFFFFFF
	
	pkg_payload = os.path.join(final_path, '%s_%0.8X' % (file_name, file_adler))
	pkg_temp = os.path.join(final_path, '__TEMP_%s_%0.8X' % (file_name, file_adler))
	os.makedirs(pkg_temp)
	
	subprocess.run(['bsdtar', '-xf', file_path, '-C', pkg_temp], check = True)
	#subprocess.run(['7z', 'x', '-aou', '-bso0', '-bse0', '-bsp0', '-o' + pkg_temp, file_path])
    
	if os.path.isfile(os.path.join(pkg_temp, 'Scripts')) :
		scripts_init = os.path.join(pkg_temp, 'Scripts')
		scripts_cpgz = os.path.join(pkg_temp, 'Scripts.gz')
		efi_path = os.path.join(pkg_temp, 'Tools', 'EFIPayloads', '')
		
		os.replace(scripts_init, scripts_cpgz)
        
		os.system('gunzip -k -q %s' % scripts_cpgz)
        
		os.system('(cd %s && cpio --quiet -id < %s)' % (pkg_temp, scripts_init))
		
		shutil.copytree(efi_path, pkg_payload)
		
	elif os.path.isfile(os.path.join(pkg_temp, 'Payload')) :
		payload_init = os.path.join(pkg_temp, 'Payload')
		payload_pbzx = os.path.join(pkg_temp, 'Payload.pbzx')
		payload_cpio = os.path.join(pkg_temp, 'Payload.cpio')
		zip_path = os.path.join(pkg_temp, 'usr', 'standalone', 'firmware', 'bridgeOSCustomer.bundle', 'Contents', 'Resources', 'UpdateBundle')
		efi_path = os.path.join(zip_path, 'boot', 'Firmware', 'MacEFI', '')
		
		os.replace(payload_init, payload_pbzx)
		
		subprocess.run(['python', 'parse_pbzx_fix.py', payload_pbzx, payload_cpio], check = True, stdout=subprocess.DEVNULL)
        
		os.system('(cd %s && cpio --quiet -id < %s)' % (pkg_temp, payload_cpio))
        
		shutil.unpack_archive(zip_path + '.zip', zip_path)
		
		if os.path.exists(efi_path) : shutil.copytree(efi_path, pkg_payload)
		
	shutil.rmtree(pkg_temp)
	
	im4p_files = []
	for root, dirs, files in os.walk(pkg_payload):
		for name in files :
			if name.endswith('.im4p') :
				im4p_files.append(os.path.join(root, name))
	
	if im4p_files : subprocess.run(['python', 'Apple_EFI_Split.py', '-skip', *im4p_files], check = True, stdout=subprocess.DEVNULL)
	for im4p in im4p_files : os.remove(im4p)
	
	final_files = []
	for root, dirs, files in os.walk(pkg_payload):
		for name in files :
			final_files.append(os.path.join(root, name))
	
	if final_files : subprocess.run(['python', 'Apple_EFI_Rename.py', '-skip', *final_files], check = True, stdout=subprocess.DEVNULL)
	
	for root, dirs, files in os.walk(pkg_payload):
		for name in files :
			if not os.path.isfile(os.path.join(final_path, name)) :
				shutil.copy2(os.path.join(root, name), os.path.join(final_path, name))
			
	shutil.rmtree(pkg_payload)

print('\nDone!')