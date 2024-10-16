 ```
Device name: Redmi Note 11 / NFC
Device codename: spes
Device maintainer: Tanvir Hasan
```

# v1.3
- Rework thermal
- Added new props
- Setup DeviceAsWebcam
- Remove cr_config.xml
- Use AOSP FLAC decoder
- Disable camera perflock
- Specify vendor.usb.device
- Limit screen recording to 60fps
- Address Maxim IC suspend policies
- Cleanup Maxim battery verify wakeup
- Migrate sensor HAL to AIDL interface
- Rebase entire Device and Vendor Tree
- Cleanup FPC fingerprint wakeup labels
- Move some Bluetooth properties to system
- Fix mialogocontrol patch when extracting blobs
- Add and increase 5 GHz network signal tolerance
- Many more underhood changes

# Notes:
- Flashing Guide [Telegram](https://telegra.ph/Flash-Rom-On-Redmi-Note-11-Spes--Spesn-07-04)
- Signed build with priv keys
- Thanks Sayan for server
- Thanks Sam, N-EX and Yograt for testing
- Thanks @CrDroidAndroid tree contributors for base trees

# v1.2
- Fixed Thumbnail Issues
- Synced with latest source
- Bootloader locked spoff
- Device MEETS STRONG INTEGRITY
- Android Security update September 2024
- Reduced status bar padding again
- Updated blobs from MIUI SPESNEEAGlobal V14.0.7.0 TGKEUXM
- Dropped bootctl package
- Changed default dexpreopt compiler filter to speed-profile
- Removed reserved partition
- Reverted back to old thermal settings
- Added can-swap-width-height for video codecs
- Enabled slow-cpu media_codecs
- Disabled NFC service by default on non spes variant
- Built some vendor modules for RIL and WFD
- Built libaudioroute from source
- Addressed powerhal denials on sepolicy
- Removed quad mic
- Corrected maximum microphone count
- Added AUDIO CHANNEL IN STEREO to BT SCO Headset Mic
- Added support for BT SCO mic for record 24 profile
- Set correct channel mask for earpiece
- Removed conditional for WfdCommon
- Many more underhood changes

# Notes:
- Clean flash recommended
- Signed build with priv keys
- Flashing Guide [Telegram](https://telegra.ph/Flash-Rom-On-Redmi-Note-11-Spes--Spesn-07-04)
- Thanks Nyao, Alberto and Yograt for testing
- Thanks @CrDroidAndroid tree contributors for base trees

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
