# Device Requirements

The key words 'MUST','MUST NOT','REQUIRED','SHALL','SHALL NOT','SHOULD','SHOULD NOT','RECOMMENDED','MAY', and 'OPTIONAL' in this document are to be interpreted as described in [RFC 2119](datatracker.ietf.org/doc/html/rfc2119).

Exceptions can be requested by contacting the Core Team.

- The device **MUST** use an ARM 64-Bit software base.

- The device **MUST** have 6 GB of RAM or more.

- The device **MUST** utilize a kernel based on version 4.4 with eBPF and binder backports, or newer versions of the Linux Kernel.

- The device **MUST** have a minimum of 128 GB of internal storage. Expansions via SD Cards **SHALL NOT** count towards this requirement.

- The device **MUST** have a minimum of approximately 9 GB of dedicated storage for the system partition, taking into account proper storage optimizations. 'RemovePackages' **SHALL NOT** be considered as such.

- The device **MUST** have SELinux set to Enforcing for release builds. However, during the alpha or beta stages, having SELinux set to Permissive is allowed.

- The device **MUST** have complete hardware compatibility equivalent to the stock ROM. For example, if 'X Hardware feature' works on stock ROM, it must also function on The Pixel Project. The only exceptions allowed are VoLTE and NFC payment methods.

- The device **MUST NOT** incorporate any unused overlays or packages. This includes, but is not limited to, unbuilt packages, non-functional packages, obsolete packages, placebo 'tweaks', or any packages that introduce unnecessary and/or undesired features, as specified in the [Maintainers Code of Conduct](https://github.com/JoeChirico/ThePixelProject-docs/blob/main/maintainers_code_of_conduct.md).

- The device sources **MUST** comply with all the relevant provisions outlined in our Maintainers Code of Conduct regarding the device source code.

- The device **MUST** support File Based Encryption (FBE). The exception to this rule is if the device originally shipped with Full Disk Encryption (FDE), provided that a proper, functional implementation of FBE is in available. Encryption must be enabled by default for all Official builds.

- The device **SHOULD NOT** necessitate a large number of patches, but if it does, source-wide patches or hacks **MUST NOT** be utilized, Device-specific patches are permitted if needed.

- It **MUST** be necessary for the device to operate correctly; otherwise, such modifications will not be accepted. For example, major changes towards CLO/CAF solely to align more closely with CLO/CAF in the device source.

**Thank you for taking the time to read The Pixel Project device requirements. We appreciate your help in making our project better.**
