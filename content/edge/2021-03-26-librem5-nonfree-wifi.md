title: "Librem 5: Action required to keep WiFi functional after upgrade"
date: 2021-03-26
---
The Librem 5 `linux-purism-librem5` kernel package 5.11.6-r1 includes a change
that causes the WiFi driver to ignore firmware on the WiFi chip and load
firmware from the rootfs. This firmware was not available in pmaports until
`device-purism-librem5` v1.18, installed by a new subpackage
`device-purism-librem5-nonfree-firmware`.

If you are upgrading an existing pmOS edge install on the Librem 5, you will
**not** have WiFi after installing this new kernel and rebooting, unless you
also install the `device-purism-librem5-nonfree-firmware` package manually
after upgrading the kernel.

Recommended steps to take:

```
$ sudo apk upgrade -a
<linux-purism-librem5 upgraded to 5.11.6-r1 here>

$ sudo apk add device-purism-librem5-nonfree-firmware
```

If you reboot before installing `device-purism-librem5-nonfree-firmware` and no
longer have functional WiFi, you can still install this package using usb
networking by manually downloading the required apks from a mirror on
[https://mirrors.postmarketos.org](https://mirrors.postmarketos.org), and using
scp to push it to the device:

```
$ curl -O http://mirror.postmarketos.org/postmarketos/master/aarch64/device-purism-librem5-nonfree-firmware-1.18-r0.apk
$ curl -O http://mirror.postmarketos.org/postmarketos/master/aarch64/firmware-siliconlabs-rs9116-2.0.0-r0.apk
$ scp device-purism-librem5-nonfree-firmware-1.18-r0.apk firmware-siliconlabs-rs9116-2.0.0-r0.apk 172.16.42.1:/tmp/
$ ssh 172.16.42.1
librem5 $ sudo apk add /tmp/device-purism-librem5-nonfree-firmware-1.18-r0.apk /tmp/firmware-siliconlabs-rs9116-2.0.0-r0.apk
```

The relevant change in pmaports is here: [merge request !2059](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2059)
