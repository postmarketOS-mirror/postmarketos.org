title: "xorg-server moved from main to community"
date: 2020-12-01
---

xorg-server and related packages were moved from main to community in Alpine
Linux. This resulted in xorg-related packages getting deleted before the new
packages were available
([aports#12152](https://gitlab.alpinelinux.org/alpine/aports/-/issues/12152)).

Until the builders have cought up and built the packages again, you can build
them yourself:

```shell-session
$ pmbootstrap pull
$ pmbootstrap aportgen --fork-alpine xorg-server xinit xauth xmodmap xrdb
$ pmbootstrap aportgen --fork-alpine libxfont2 xcb-util-image xcb-util-keysyms xcb-util-renderutil xcb-util-wm
$ pmbootstrap build --arch=aarch64 xorg-server
```

If cross compiling xorg-server fails in the last step, add `!check` to the
`options` in `temp/xorg-server/APKBUILD` of your local
[pmaports.git](https://wiki.postmarketos.org/wiki/Pmaports.git) clone.
