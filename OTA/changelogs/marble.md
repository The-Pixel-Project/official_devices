 ```
Device name: Poco F5/ Redmi Note 12 Turbo
Device codename: marble
Device maintainer: kenway214
```

## v1.1

**Device Changelog 16.08.2024**

- Fix battery and USB OTG detection
- Drop xiaomi libsensor_cal@2.0.so
- Build xiaomi-telephony-stub
- wifi: Enable support for IEEE80211AX
- audio: Disable DRC
- audio: Fix mic issues in apps like WhatsApp
- Explicitly disable GL comp backpressure
- overlay: Enable Night Display and Extra Dim
- rootdir: Add sdcard1 and usbotg to recovery fstab
- Load adsp_loader_dlkm for battery status in recovery
- sensors: Increase _oem_msg struct size
- Kill xiaomi citsensorservice and sensor communicate
- sensors: Introduce LightNotifier and use libssccalapi@2.0
- sensors: Add aod notifier
- sensors: Convert nonui notifier into a generalized sensor based notifier
- sensors: Close touch dev fd after usage
- Use kernel provided xiaomi_touch.h
- sensors: Pass nonui value unmodified to touchscreensensors: Pass nonui value unmodified to touchscreen
- sensors: Cleanup code and drop unused dependencies
- Drop nfc services from manifest
- Migrate to QTI USB Gadget 1.2 HIDL
- Swap to QTI USB init scripts
- Assert for marble or marblein
- Introduce sensor notifier extension to report raw brightness
- Set HWC-specific properties
- Add missing kvh2xml.xml
- Add Xiaomi sensor module

## v1.0

**Device Changelog 08.08.2024**

- Auto brightness much more responsive
- Tuned haptics
- Fixed aod blinking
- Switched to xiaomi dolby with graphical eq
- Removed Misound enhancer

**Device Changelog 03.08.2024**

- Fixed haptics
- Fixed AOD
- Fixed dt2w and dt2s
- Fixed Auto brightness
- Fixed manual saturation slider sometimes reset
- Fixed Google recorder Speech recognition
- Fixed miui Camera OIS

**Device Changelog 28.07.2024**

- Initial Official build
- Includes oneplus dolby
- Added Qcom audio effects from oneplus 9R
- Added Mi Sound Enhancer
- Added new manual saturation display slider

# Notes:
- Signed Build
- Flashing Guide [#guide](https://github.com/kenway214/marble_updates/blob/main/Flashing_Guide_Marble_A14.md)
