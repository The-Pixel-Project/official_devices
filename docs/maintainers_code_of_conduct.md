# Maintainers Code of Conduct: 

The key words 'MUST','MUST NOT','REQUIRED','SHALL','SHALL NOT','SHOULD','SHOULD NOT','RECOMMENDED','MAY', and 'OPTIONAL' in this document are to be interpreted as described in [RFC 2119](datatracker.ietf.org/doc/html/rfc2119).

The Pixel Project device maintainers:

- **MUST NOT** get involved in arguments or resort to insults, or use hateful words, personal attacks or any other verbal or nonverbal action that is considered detrimental towards the creation of a positive environment for the team. If at all a situation arises, involving someone from the Administration team to help sort it out is recommended.

- **MUST** upload: 
     
     - All device sources on [TPP-Devices](https://github.com/TPP-Devices). It goes without saying that these should be fully buildable. External repositories for build releases are prohibited. Exceptions may be open only if it's absolutely necessary.

     - Changelogs for each build. These MUST be user friendy, simplifying changes for the average users who may not be familiar with concepts like PlayIntegrity or color calibration but wish to know what has changed since the last update.
    
- **MUST** test every build before sending an OTA update to users. Each build must undergo thorough testing by the maintainer to ensure all hardware and software functionalities are operational before release. Releasing untested builds will result in revocation of maintainership.

- **MUST** deliver updated buils for their device on a monthly basis or whenever a new update is released. If this is not feasible, reasons must be communicated to The Pixel Project Core Team. In the absence of any explanation for 3 months, the maintainer will be kicked without any prior warning. The same applies if an unsatisfactory reason is given.

- **MUST** maintain authorship of all git commits pushed, this is a mandatory for ALL repositories

- In case of disputes between maintainers, resolve them privately via direct messages on Telegram or XDA. Avoid bringin disputes to our chats. The same applies to public chats, contact The Pixel Project Core Team for prompt resolution.

- **MUST NOT** include: 
     
     - Any script that removes packages provided by the ROM source without prior approval from The Pixel Project Core Team, e.g. RemovePackages.

     - Features in device-specific packages, eg. configpanel, XiaomiParts etc.

     Device-specific features available in stock firmware, e.g. Alert Slider and Offscreen gestures for select OnePlus Devices,
     Fingerprint Gestures and MotoActions for Motorola Devices are allowed.

     Dirac Sound or any audio enhancer feature **MUST** be fully functional or a native feature of the device's Stock ROM (and still be fully functional); otherwise, it's prohibited.

     - Playground or anything else related to getting Pixel-like features that aren't available from the ROM sources (Instead, notify us of such features) - Only GoogleCamera and ARCore are acceptable.

     - Any Google applications not available from ROM sources; only GoogleCamera is acceptable, but please ensure that you use a reliable source and that the device has proper support for them.

     - Any stock firmware app. Once again GoogleCamera is acceptable per se, so is the camera app from the stock firmware itself, only, if fully functional.


- **MUST NOT** include Overclock/Underclock/Undervolt for CPU/GPU/Display in the kernel source.

- **MUST NOT** include any changes to charging voltages.

- **MUST NOT** include KernelSU or any other method to get superuser privileges.

- About Magisk, the maintainers **MUST NOT**:
     
     - Includ Magisk in the build.
      
     - Perform significant software modifications solely to enable Magisk. If incompatible, users should be advised to refrain from using Magisk.
      
     - Intentionally modify configurations to prevent Magisk from functioning, lusers must have the freedom to choose whether to install it (though the Team does not endorse its use).

- **MUST NOT**  ship any other recovery other than the AOSP Recovery provided by us.

Failure to comply with any of these rules will result in immediate action from The Pixel Project Core Team against the maintainer, without prior warning.

**Thank you for taking the time to read The Pixel Project maintainers code of conduct. We appreciate your help in making our project better.**
