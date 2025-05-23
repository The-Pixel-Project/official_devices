### Requirements:

* Unlocked bootloader
* A pc with platform-tools and all the necessary device drivers installed (adb/fastboot)

### First time installation (clean flash):

* Boot to Fastboot mode
* Flash the vendor_boot image:

```
fastboot flash vendor_boot vendor_boot.img
```
* Flash the DTBO image:

```
fastboot flash dtbo dtbo.img
```
* Flash the boot image:

```
fastboot flash boot boot.img
```
* Reboot to recovery:

```
fastboot reboot recovery
```
* In recovery mode, navigate to **Factory reset -> Format data/factory reset** and confirm to format the device.
* After formatting, return to the main menu and navigate to **Apply update -> Apply from ADB**.
* Sideload the ROM:

```
adb sideload The-Pixel-Project.zip (replace "The-Pixel-Project" with the actual filename)
```
* Reboot to recovery to sideload any add-ons (e.g., Magisk, Firmware etc).
* Finally, reboot to the system.

### Updating (dirty flash):
#### Via recovery (recommended way):
* Boot to recovery
* Choose apply update and Apply from ADB
* Now install The-Pixel-Project.zip via sideload and reboot

```
adb sideload The-Pixel-Project.zip
```

#### Via OTA:
* Go to Settings -> System -> System updates and download latest build
* Choose install and let it finish
* Reboot & enjoy
