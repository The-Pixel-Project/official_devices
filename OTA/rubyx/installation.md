# ROM installation

## Download the required files

- boot.img
- vbmeta.img (optional, only needed for first install)
- ROM.zip file (eg: for The Pixel Project : PixelProject_rubyx-2.2-OFFICIAL-20250615-1124.zip)



## Flashing recovery

- Reboot into fastboot mode
- Flash vbmeta.img (optional, only needed for first install) using this command (fastboot flash vbmeta path_to_vbmeta.img)
- Flash the Recovery using this command (fastboot flash boot path_to_boot.img)
- Reboot the phone into recovery using this command (fastboot reboot recovery)
- Format data: Factory reset -> Format data/factory reset
- Go back to the main menu. Then sideload the zip: Apply update -> Apply from ADB
- In your cmd, use this command to sideload the rom (adb sideload path_to_rom.zip)
- Now you can reboot your phone with Reboot to system option can be found at recovery main menu.
- Enjoy!


**Dirty Flash :**
- Go to local updater and select the proper ROM zip

### OR
- Go to the recovery.
- Do adb sideload rom.zip
- Reboot to system and enjoy.