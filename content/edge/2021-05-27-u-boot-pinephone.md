title: "PinePhone/PineTab: U-Boot gets upgraded in post-install"
date: 2021-05-27
---

A new feature has been implemented in postmarketOS edge
([!2155](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2155)):
new U-Boot versions will be rolled after upgrading u-boot-pinephone, which is
used for both the PinePhone and PineTab.

Before this change, the bootloader would only get updated after running
`update-u-boot` manually (which is still possible and can be used to change the
[RAM clock frequency](https://wiki.postmarketos.org/wiki/PINE64_PinePhone_(pine64-pinephone)#Changing_the_Clock_Frequency))
or when flashing a new postmarketOS image.

Great care has been taken to ensure that this works, there's even a checksum
verification after rolling out the new version. If something should go wrong
however, the wiki explains how to
[restore U-Boot](https://wiki.postmarketos.org/wiki/PINE64_PinePhone_(pine64-pinephone)#Fix_U-Boot).

This change has been implemented, so we can ensure everybody is on latest
crust-firmware/arm-trusted-firmware before upgrading to the 5.12 series of
megi's kernel tree. He noted that otherwise phones will overheat.
