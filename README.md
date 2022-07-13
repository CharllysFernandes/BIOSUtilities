# BIOSUtilities
**Various BIOS Utilities for Modding/Research**

[BIOS Utilities News Feed](https://twitter.com/platomaniac)

* [**Dell PFS Update Extractor**](#dell-pfs-update-extractor) [use Dell_PFS_Extract from refactor branch]
* [**AMI UCP BIOS Extractor**](#ami-ucp-bios-extractor) [use AMI_UCP_Extract from refactor branch]
* [**AMI BIOS Guard Extractor**](#ami-bios-guard-extractor) [use AMI_PFAT_Extract from refactor branch]
* [**Phoenix SCT BIOS Extractor**](#phoenix-sct-bios-extractor) [use Phoenix_TDK_Extract from refactor branch]
* [**Insyde iFlash Image Extractor**](#insyde-iflash-image-extractor) [use Insyde_IFD_Extract from refactor branch]
* [**Portwell EFI BIOS Extractor**](#portwell-efi-bios-extractor) [use Portwell_EFI_Extract from refactor branch]
* [**Panasonic BIOS Update Extractor**](#panasonic-bios-update-extractor) [use Panasonic_BIOS_Extract from refactor branch]
* [**VAIO Packaging Manager Extractor**](#vaio-packaging-manager-extractor) [use VAIO_Package_Extract from refactor branch]
* [**Fujitsu UPC BIOS Extractor**](#fujitsu-upc-bios-extractor) [use Fujitsu_UPC_Extract from refactor branch]
* [**Fujitsu SFX BIOS Extractor**](#fujitsu-sfx-bios-extractor) [use Fujitsu_SFX_Extract from refactor branch]
* [**Award BIOS Module Extractor**](#award-bios-module-extractor) [use Award_BIOS_Extract from refactor branch]
* [**Apple EFI Package Grabber**](#apple-efi-package-grabber)
* [**Apple EFI File Renamer**](#apple-efi-file-renamer)
* [**Apple EFI IM4P Splitter**](#apple-efi-im4p-splitter)
* [**Apple EFI Package Extractor**](#apple-efi-package-extractor)

## **Dell PFS Update Extractor**

#### **!!! OUTDATED !!!**

[Please use Dell_PFS_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **AMI UCP BIOS Extractor**

#### **!!! OUTDATED !!!**

[Please use AMI_UCP_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **AMI BIOS Guard Extractor**

#### **!!! OUTDATED !!!**

[Please use AMI_PFAT_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Phoenix SCT BIOS Extractor**

#### **!!! OUTDATED !!!**

[Please use Phoenix_TDK_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Insyde iFlash Image Extractor**

#### **!!! OUTDATED !!!**

[Please use Insyde_IFD_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Portwell EFI BIOS Extractor**

#### **!!! OUTDATED !!!**

[Please use Portwell_EFI_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Apple EFI Package Grabber**

![](https://i.imgur.com/BaHrjGi.png)

#### **Description**

Parses user-provided (DB) list of Apple Software Update CatalogURL .sucatalog links and saves all newer (since last run) EFI firmware package links into a text file. It removes any xml formatting, ignores false positives, removes duplicate links and sorts them in alphabetical order for easy comparison afterwards.

#### **Usage**

First, you need to familiarize a bit with the DB (i.e. Apple_EFI_Grab.dat file). It consists of 3 sections: Last run DateTime (YYYY-MM-DD HH:MM:SS), Sucatalog links to check and EFI Package links which have been gathered so far across all runs. Before running the utility for the fist time, you need to insert the Sucatalog links into the DB, below the 1st line (DateTime). The Sucatalog links in the DB are stored in partial form, starting from "index" string. For example: "https://swscan.apple.com/content/catalogs/others/index-12.merged-1.sucatalog" must be stored as "index-12.merged-1.sucatalog" in the DB. The Sucatalog links are not pre-included in the DB but you can find them online (e.g. https://github.com/zhangyoufu/swscan.apple.com/blob/master/url.txt).

#### **Compatibility**

Should work at all Windows, Linux or macOS operating systems which have Python 3.7 support.

#### **Prerequisites**

To run the python script, you need to have the following 3rd party Python module installed:

* [pefile](https://pypi.org/project/urllib3/)

> pip3 install urllib3

#### **Build/Freeze/Compile with PyInstaller**

PyInstaller can build/freeze/compile the utility at all three supported platforms, it is simple to run and gets updated often.

1. Make sure Python 3.7.0 or newer is installed:

> python --version

2. Use pip to install PyInstaller:

> pip3 install pyinstaller

3. Use pip to install urllib3:

> pip3 install urllib3

4. Build/Freeze/Compile:

> pyinstaller --noupx --onefile Apple_EFI_Grab.py

At dist folder you should find the final utility executable

#### **Anti-Virus False Positives**

Some Anti-Virus software may claim that the built/frozen/compiled executable contains viruses. Any such detections are false positives, usually of PyInstaller. You can switch to a better Anti-Virus software, report the false positive to their support, add the executable to the exclusions, build/freeze/compile yourself or use the Python script directly.

## **Apple EFI File Renamer**

![](https://i.imgur.com/mWGhWja.png)

#### **Description**

Parses Apple EFI files and renames them based on Intel's official $IBIOSI$ tag as follows: Model_Version_Build_Year_Month_Day_Hour_Minute_Checksum. The checksum is calculated and added by the utility in order to differentiate any EFI files with the same $IBIOSI$ tag. In rare cases in which the $IBIOSI$ tag is compressed, the utility automatically first uses [LongSoft's UEFIFind and UEFIExtract](https://github.com/LongSoft/UEFITool) tools.

#### **Usage**

You can either Drag & Drop or manually enter the full path of a folder containing Apple EFI firmware.

#### **Download**

An already built/frozen/compiled binary is provided by me for Windows only. Thus, **you don't need to manually build/freeze/compile it under Windows**. Instead, download the latest version from the [Releases](https://github.com/platomav/BIOSUtilities/releases) tab. To extract the already built/frozen/compiled archive, you need to use programs which support RAR5 compression. Note that you need to manually apply any prerequisites.

#### **Compatibility**

Should work at all Windows, Linux or macOS operating systems which have Python 3.7 support. Windows users who plan to use the already built/frozen/compiled binary must make sure that they have the latest Windows Updates installed which include all required "Universal C Runtime (CRT)" libraries.

#### **Prerequisites**

To run the python script or its built/frozen/compiled binary, you need to have the following 3rd party tools at the same directory:

* [UEFIFind](https://github.com/LongSoft/UEFITool) (i.e. UEFIFind.exe)
* [UEFIExtract](https://github.com/LongSoft/UEFITool) (i.e. UEFIExtract.exe)

#### **Build/Freeze/Compile with PyInstaller**

PyInstaller can build/freeze/compile the utility at all three supported platforms, it is simple to run and gets updated often.

1. Make sure Python 3.7.0 or newer is installed:

> python --version

2. Use pip to install PyInstaller:

> pip3 install pyinstaller

3. Build/Freeze/Compile:

> pyinstaller --noupx --onefile Apple_EFI_Rename.py

At dist folder you should find the final utility executable

#### **Anti-Virus False Positives**

Some Anti-Virus software may claim that the built/frozen/compiled executable contains viruses. Any such detections are false positives, usually of PyInstaller. You can switch to a better Anti-Virus software, report the false positive to their support, add the executable to the exclusions, build/freeze/compile yourself or use the Python script directly.

## **Apple EFI IM4P Splitter**

![](https://i.imgur.com/G5RkXQk.png)

#### **Description**

Parses Apple multiple EFI firmware .im4p files and splits all detected EFI firmware into separate SPI/BIOS images.

#### **Usage**

You can either Drag & Drop or manually enter the full path of a folder containing Apple EFI IM4P firmware.

#### **Download**

An already built/frozen/compiled binary is provided by me for Windows only. Thus, **you don't need to manually build/freeze/compile it under Windows**. Instead, download the latest version from the [Releases](https://github.com/platomav/BIOSUtilities/releases) tab. To extract the already built/frozen/compiled archive, you need to use programs which support RAR5 compression. Note that you need to manually apply any prerequisites.

#### **Compatibility**

Should work at all Windows, Linux or macOS operating systems which have Python 3.7 support. Windows users who plan to use the already built/frozen/compiled binary must make sure that they have the latest Windows Updates installed which include all required "Universal C Runtime (CRT)" libraries.

#### **Prerequisites**

To run the utility, you do not need any 3rd party tool.

#### **Build/Freeze/Compile with PyInstaller**

PyInstaller can build/freeze/compile the utility at all three supported platforms, it is simple to run and gets updated often.

1. Make sure Python 3.7.0 or newer is installed:

> python --version

2. Use pip to install PyInstaller:

> pip3 install pyinstaller

3. Build/Freeze/Compile:

> pyinstaller --noupx --onefile Apple_EFI_Split.py

At dist folder you should find the final utility executable

#### **Anti-Virus False Positives**

Some Anti-Virus software may claim that the built/frozen/compiled executable contains viruses. Any such detections are false positives, usually of PyInstaller. You can switch to a better Anti-Virus software, report the false positive to their support, add the executable to the exclusions, build/freeze/compile yourself or use the Python script directly.

## **Apple EFI Package Extractor**

![](https://i.imgur.com/pufGuZ4.png)

#### **Description**

Parses Apple EFI firmware packages (i.e. FirmwareUpdate.pkg, BridgeOSUpdateCustomer.pkg), extracts their EFI images, splits those in IM4P format and renames the final SPI/BIOS images accordingly. The utility automatically uses the free version of [AnyToISO](https://www.crystalidea.com/anytoiso) to extract the EFI .pkg files. The subsequent IM4P splitting and EFI renaming requires the presence of "Apple EFI IM4P Splitter" and "Apple EFI File Renamer" utilities.

#### **Usage**

You can either Drag & Drop or manually enter the full path of a folder containing Apple EFI firmware package (.pkg) files. Depending on where AnyToISO is installed on your system, you must change the "anytoiso_path" variable accordingly.

#### **Download**

An already built/frozen/compiled binary is **not** provided because the script requires the user to set the AnyToISO executable path variable. Remember that you need to include prerequisites such as AnyToISO, Apple EFI IM4P Splitter and Apple EFI File Renamer for the utility to work.

#### **Compatibility**

Should work at all Windows & macOS operating systems which have Python 3.7 and AnyToISO support.

#### **Prerequisites**

To run the python script, you need to have the following 3rd party tools installed or placed at the same directory:

* [AnyToISO](https://www.crystalidea.com/anytoiso) (i.e. anytoiso.exe)
* [UEFIFind](https://github.com/LongSoft/UEFITool) (i.e. UEFIFind.exe)
* [UEFIExtract](https://github.com/LongSoft/UEFITool) (i.e. UEFIExtract.exe)

#### **Build/Freeze/Compile with PyInstaller**

PyInstaller can build/freeze/compile the utility at all three supported platforms, it is simple to run and gets updated often. Note that, due to this utility's nature, you may need to perform some small script changes for a built/frozen/compiled binary to work.

1. Make sure Python 3.7.0 or newer is installed:

> python --version

2. Use pip to install PyInstaller:

> pip3 install pyinstaller

3. Build/Freeze/Compile:

> pyinstaller --noupx --onefile Apple_EFI_Package.py

At dist folder you should find the final utility executable

#### **Anti-Virus False Positives**

Some Anti-Virus software may claim that the built/frozen/compiled executable contains viruses. Any such detections are false positives, usually of PyInstaller. You can switch to a better Anti-Virus software, report the false positive to their support, add the executable to the exclusions, build/freeze/compile yourself or use the Python script directly.

## **Panasonic BIOS Update Extractor**

#### **!!! OUTDATED !!!**

[Please use Panasonic_BIOS_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **VAIO Packaging Manager Extractor**

#### **!!! OUTDATED !!!**

[Please use VAIO_Package_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Fujitsu UPC BIOS Extractor**

#### **!!! OUTDATED !!!**

[Please use Fujitsu_UPC_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Fujitsu SFX BIOS Extractor**

#### **!!! OUTDATED !!!**

[Please use Fujitsu_SFX_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)

## **Award BIOS Module Extractor**

#### **!!! OUTDATED !!!**

[Please use Award_BIOS_Extract from refactor branch](https://github.com/platomav/BIOSUtilities/tree/refactor)