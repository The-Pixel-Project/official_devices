### Pre-installation:

* Recovery
* Android 13 version of stock OS
* Odin3 [Download](https://undocumented.software/Odin_3.13.1.zip)


### First time installation (clean flash):

* Backup your data to PC, OTG flash drive
* Boot to download mode and flash recovery via Odin
* Now boot to recovery by holding volume up + power button
* Navigate to Factory reset and format data, wipe system
* Reboot to recovery
* Navigate to Apply update and choose from adb
* Sideload PixelProject zip

```	
adb sideload PixelProject
```

* Reboot to system

### Update installation:
#### Via recovery (recommended way):

* Boot to download mode and flash recovery via Odin
* Boot to recovery by holding Volume up + Power button
* Navigate to Apply update and choose from adb
* Sideload PixelProject zip and reboot

```
adb sideload PixelProject.zip
```

#### Via OTA:

* Go to Settings -> System -> Updater and download latest build
* Choose install and let it finish
* Reboot
