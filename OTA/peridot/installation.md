# Flashing Intruction


1. Reboot to fastboot
2. Flash the provided recovery image via fastboot using "fastboot flash recovery recovery.img" 
3. Reboot to recovery using either volume + and power button combo or via fastboot command "fastboot reboot recovery"
4. Navigate to Apply Update  > Apply from ADB
5. adb sideload the rom zip using "adb sideload PixelProject-2-*-peridot.zip" 
6. At the end of the flashing step when ask (reboot to recovery for additional packages ... yes/no)  select YES... this will reboot back to recovery with boot slot changed
7. Now sideload the rom zip using "adb sideload PixelProject-2-*-peridot.zip"  (AGAIN) (TOTAL 2 TIMES)
8. At the end of the flashing step when ask (reboot to recovery for additional packages ... yes/no)  select NO
9. Factory reset/format data
10. Reboot to system


Note:
Rom includes firmware file no need to flash anything just follow steps carefully

This build needs flashing 2 times (both slot).. 

Dirty Flash
from next builds.. (when doing dirty flash)

Reboot to recovery using either volume + and power button combo or via fastboot command "fastboot reboot recovery"
Navigate to Apply Update  > Apply from ADB
adb sideload the rom zip using "adb sideload PixelProject-2-*-peridot.zip" 
Reboot to system



EDIT