title: "util-linux from Alpine Linux aports installs binaries in wrong location"
date: 2021-06-26
---

The `util-linux-misc-2.37-1` in Alpine Linux aports installs binaries
this package provides (e.g.  `losetup`, `agetty`) into the wrong location on
the rootfs.

This breaks many `pmbootstrap` commands that need the non-busybox version of
these tools:

```
$ pmbootstrap -y zap && yes 1|pmbootstrap -y install --fde
(3714044) [19:39:39] (native) % losetup --json --list
losetup: unrecognized option: json
BusyBox v1.33.1 () multi-call binary.

Usage: losetup [-rP] [-o OFS] {-f|LOOPDEV} FILE: associate loop devices
...
```

The `util-linux-misc-2.37-2` update fixes this problem.

If this broken package was installed on an existing pmOS installation, there
may be unintended consequences. Please stop by the [pmOS chat](https://wiki.postmarketos.org/wiki/Matrix_and_IRC) 
or
[file an issue on our gitlab](https://gitlab.com/postmarketOS/pmaports/-/issues) if you
experience problems from this and need help.


The local chroots from pmbootstrap will also be broken if this package was
installed. This means that `zap` will not work. You can either remove the
pmbootstrap working directory, or upgrade `util-linux` and then run zap with:

```
$ pmbootstrap chroot -- apk update
$ pmbootstrap chroot -- apk upgrade -a
$ pmbootstrap zap
```

Also see:

- [aports!22630](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/22630)
