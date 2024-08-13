 ```
Device name: Redmi Note 11 / NFC
Device codename: spes
Device maintainer: Tanvir
```

# v1.1
- Overlay improvement
- Applied August Security Patch QPR3
- props: Tweak lmk props
- Move to common Xiaomi light AIDL
- props: Disable dynamic refreshrate
- Revert props: Set higher priority to c2 than OMX
- Revert codecs: Nuke software OMX codecs
- sepolicy: Remove duplicate sysfs_kgsl
- overlay: Nuke max cached processes override
- Remove wait_for_keymaster and all references
- sepolicy: Allow surfaceflinger to access firmware
- sepolicy: Update hal_power_default to have sys_admin capability
- Misc Improvements

# Notes:
- Signed Build
- Dirty Flash Works
- Flashing Guide [Telegram](https://telegra.ph/Flash-Rom-On-Redmi-Note-11-Spes--Spesn-07-04)
- Do not report bugs caused by third-party mods or modules
- Thanks @CrDroidAndroid tree contributors for base trees
- Thanks @Yogratdesuyo @xdlane @pratikanurag & @Faikar_M for Testing
