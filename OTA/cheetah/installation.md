# Flashing Intruction

1. Download all the Images from Recovery folder in SourceForge.
2. Go to the Folder where you have saved those Images and Open terminal in that Folder.
3. Execute these commands -
   `fastboot flash boot boot.img && fastboot flash dtbo dtbo.img && fastboot flash init_boot init_boot.img && fastboot flash vendor_boot vendor_boot.img && fastboot flash vendor_kernel_boot vendor_kernel_boot.img`
4. Reboot to recovery with this command -
   `fastboot reboot recovery`
5. Follow Accordingly — [clean_flash](#clean-flash) | [dirty_flash](#dirty_flash)

## Clean Flash

0. Make Sure you Followed the [Flashing Intruction](#flashing-intruction)
1. Reboot to Recovery.
2. Click on apply update —> apply from ADB —> execute command - adb sideload PixelProject.zip .
3. After completion —> Click NO —> Go to F*actory Reset* —> Wipe Data.
4. Reboot your Device. Done ✅

## Dirty Flash

1. Reboot to Recovery.
2. Click on apply update —> apply from ADB —> execute command - adb sideload PixelProject.zip .
3. After completion —> Click NO.
4. Reboot your Device. Done ✅
