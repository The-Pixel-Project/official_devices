## 01-06-25


- Latest source changes
- May security patch (QPR2) ,HyperOS 2 based
- Updated blobs from OS2.0.103.0.VNPMIXM
- Updated firmware from OS2.0.102.0.VNPMIXM
- Dropped firmware from rom zip
- touchsampling: Add per app high touch sampling support
- touchsampling: Refactor and dropped all old mothods
- powertools: Introduce per-app power profile support and bump version to v6
- powertools: Tuned Balanced , Gameboost , performance profile for case specific scnerios
- powertools: Balanced: sustained lower clock if high demand process for better sustained battery ,hooked with libperfmanager
- powertools: Gameboost: Added lauchboost , load priority, cache management for apps using game boost powerprofile
- powertools: performance: using mgame sconfig thermal fallback ,hooked with libperfmanager for sustained high performance without much heating
- powertools: Batterysaver: added seperate toggle weather to enable android system battery saver when this power profile is set
- thermalprofile: Dropped per app thermal profile
- GameBar: Introduce Ram temp and Ram clock speed overlay
- GameBar: Create gamebargesturehandler to address all Gestures
- GameBar: Refactor and bump version to v6
- Revert "peridot: parts: Introduce RefreshRateService to enforce 120Hz on screen wake events"
- Revert "peridot: parts: Introduce RefreshRate QS tile"
- TurboCharging: Consolidated turbo and sports mode logic into applyAllSettings()
- TurboCharging: Simplified BootReceiver by offloading logic to TurboChargingUtil
- TurboCharging: Introduced ChargerReceiver to re-apply settings on POWER_CONNECTED
- TurboCharging: Updated QS tile to re-apply both turbo and sports modes on toggle
- Add support for 60Hz in Landscape in per app refresh rate
- Dropped config_autoBrightnessAdjustmentMaxGamma
- Introduce RefreshRateService to enforce 120Hz on screen wake events (attempt to fix 30Hz bug when using adaptive refrest rate, after unlock 30hz bug may be there for 1 sec if this happenes service will trigger and correct itselt to 120Hz within next sec.so device will not stuck at 30Hz)
- Touchfeature: Intoducing Xiaomi touch control via ITouchFeature aidl (settings/display/Touch control)
- Touchfeature: Refactors the initialization logic for Double Tap to Wake and SoFOD features into standalone services—DoubleTapService and SoFodTouchService.
- Touchfeature: DoubleTapService registers a content observer for the DOUBLE_TAP_TO_WAKE setting and applies the corresponding touch mode via ITouchFeature 14
- Touchfeature: SoFodTouchService enables SoFOD-related touch modes via ITouchFeature 10 11 16
- Touchfeature: Minor cleanup and improved logic and logspam
- Enable Client Composition Cache
- udfps: Enable HBM via disp_feature
- udfps: Defer extCmd until fod ui is ready
- udfps: Drop unnecessary setFingerDown on cancel
- udfps: Fix wrong udfps debugging
- udfps: Avoid partial reads on disp_feature
- udfps: Fix stack memory address return in UdfpsHandler
- udfps: Disable lhbm when authentication is finished
- udfps: Disable lhbm on most acquired events
- init: Give proper permissions for /dev/mhi_*_pipe_4 
- Enable HWUI adpf
- Import missing feature_enabler_client.rc
- fstab: Switch to ext4


## 17-05-25

- Latest source changes
- May security patch (QPR2) ,HyperOS 2 based
- Move Lineage Health HAL to select()
- Set libinit via soong config
- Add libwfdservice_shim for WFD
- Parts: Refactor touchsampling code (touch sampling now 500 tsr)
- Fixed focaltech panels touch not working ( audio still dead fs19xx audio drivers)
- Enable sofod using stock kernel node
- Build udfps sensor from hardware xiaomi
- Switched to stock kernel Hyper OS2.0.102.0.VNPMIXM
- fstab: Switch to erofs
- Drop full qti perf hal stack
- Improved active drain
- Migrate to common libqti-perfd-client and power-libperfmgr
- Inherit dummy powerhint config
- Inital powerhint for cliff platform (credit: @ahmed_tohamy)
- utilize task_profiles.json + cgroups.json
- sepolicy: Allow libperfmgr to write on /proc & sysfs
- Optimize cpu up_rate_limit and down_rate_limit
- Register and enable qcrild & data services
- Add missing layer buffer slots cache clear property
- Enable frame pacing
- Fix the battery drain due to statsd
- Patch algo jni lib to use correct Surface::connect method
- Add Ultra HDR heic configurations to StreamConfigurationMap constructor
- ICustomCaptureResult: Add readout timestamp
- Add Soong namespace imports for required hardware components 
- Enable volume set param for compressed, pcm offload and voip streams
- Use separate calibration for bluetooth a2dp low latency 
- audio: Use EC enabled streams for hotword capture and single mic in lp mode
- Align CPU frequency values and entries with corrected hardware frequencies
- udfps: Notify HAL on both FOD press and release events
- udfps: Disable local HBM immediately on successful auth
- Updated and patched dolby blobs
- Fixed Dolby atmos crashed issue
- Powertools fixed cpu boost freq not loading correctly
- Fixed jittery Ui due to cpu freq mismatch with powerprofiles
- powerprofile optimise gaming profile

## 27-04-25

-   April security patch
-   overlay: Disable turbulence noise
-   Fixed inadjustable volume control on voip speaker calls
-   Fixed Charging Control now works → Set charging limit to 80% or above (below 80% not currently supported).
-   Added Turbo Charging Support with selectable max wattage: 18W / 33W / 45W / 60W / 90W.
-   Added Shake Gesture for Torch
-   Compile HWUI for performance -fno-omit-frame-pointer, -marm, -mapcs
-   Screen-off UDFPS via AOD hack: Enable Settings > Gestures > Always-On Fingerprint
-   Always-On Fingerprint(AOF) - Enabling Always-On Fingerprint: Increases screen-off battery drain , Prevents ambient notifications from showing. Disable it if you want Always-On Display (AOD) to function. Added SOFOD p icon (auto hide option now 15 sec ,30 sec, 1 min (extra))
-   Switch to common xiaomi vibrator service
-   Adapt to xiaomi vibrator effects
-   Import init.peridot.rc
-   Import missing com.nxp.nfc.nq.xml permission
-   Enable ro.surface_flinger.clear_slots_with_set_layer_buffer
-   Drop rfs_msm_mpss_readonly_modem_firmware_symlink
-   move mpss symlink back to android.mk
-   qril: Generate qcrilNr.db during build
-   qril: Add migration to turn off redir_party_num
-   qril: Turn off persist.vendor.radio.poweron_opt
-   Drop OMX Dependencies for latest sources
-   kang auto-brightness configs from houji
-   props: Disable FRP
-   PowerTools- Bump version to v3.0
-   PowerTools- Full codebase refactor for the PowerTools module
-   PowerTools- Added 'Unknown' mode: if any external module modifies PowerTools behavior unexpectedly, the mode will automatically switch to 'Unknown' to reflect the change
-   Game Bar v4.0 – Complete rework of the entire codebase for better performance and maintainability.
 Added two FPS tracking methods: You can now switch between FPS measurement methods via the Game Bar settings under the "FPS Measurement Type" option
   1. Modern Android API-based method
Uses the official Android API for FPS tracking
More accurate and reliable than traditional methods
⚠️ Note: When this method is active, other FPS tools (e.g., GameSpace FPS meter, Scene, etc.) may not work due to exclusive access to system counters
   2. Legacy system-based method (for broader compatibility)
Compatible with most third-party FPS tracking apps
Recommended if you're using external tools alongside Game Bar
-   Game Bar- Improved draggable overlay: Overlay can now be moved freely (bugfix) and placed anywhere on the screen (select customisaton/ovrlay position/custom draggable)
-   Game Bar-Auto-launch Game Bar for selected apps:
      - Game Bar can now automatically launch when a selected app is opened
      - Add apps from the bottom section of the Game Bar menu
      - Toggle the Auto Enable switch to allow launch even when the main Game Bar    toggle is off
-   parts: Bumped minSdkVersion to 33 and targetSdkVersion to 35 to support modern APIs.
-   Updated privapp whitelist to grant necessary permissions for new features
-   Fixed dolby.media.c2@1.0-service crashing

## 06-04-25

-   Initial A15 Release QPR2 march security patch.

