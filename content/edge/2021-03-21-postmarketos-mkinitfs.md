title: "No space left on boot partition"
date: 2021-03-21
---
In Alpine edge, LLVM was recently upgraded from 10 to 11. The new libLLVM-11.so
is bigger than libLLVM-10.so, which triggered a bug on the PinePhone and
possibly other devices where hardware acceleration for osk-sdl is enabled.
During upgrades, if a new initramfs was generated, it would run out of space on
/boot:

```
==> initramfs: creating /boot/initramfs-postmarketos-allwinner-extra
gzip: write error: No space left on device
cpio: write error: Broken pipe
```

Make sure you have at `postmarketos-mkinitfs` version `0.22-r1` or higher
installed, where we resolved this issue
([pmaports!2051](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2051)).
If you ran into this issue and your device does not boot anymore, restore the
boot partition. For the PinePhone, see
[this guide](https://wiki.postmarketos.org/wiki/PINE64_PinePhone_(pine64-pinephone)#Fix_broken_boot_partition).

Details in
[pmaports#1018](https://gitlab.com/postmarketOS/pmaports/-/issues/1018).
