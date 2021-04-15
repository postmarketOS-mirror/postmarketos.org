title: "pipewire-pulse used instead of pipewire in new pmbootstrap installs"
date: 2021-04-15
---
When building postmarketOS images with the Phosh UI, pipewire-pulse gets
installed instead of pulseaudio. This results in broken audio.

<del>Existing installs and pre-built images are not affected.</del>

More information: [#1067](https://gitlab.com/postmarketOS/pmaports/-/issues/1067)

**UPDATE 2021-04-16:** still working on a fix, and current images from edge are
affected. Run this as workaround, followed by reboot:

```
$ sudo apk update
$ sudo apk add !pipewire-pulse
(1/7) Purging pipewire-pulse (0.3.25-r0)
(2/7) Installing pulseaudio-alsa (14.2-r5)
(3/7) Installing webrtc-audio-processing (0.3.1-r0)
(4/7) Installing pulseaudio (14.2-r5)
Executing pulseaudio-14.2-r5.post-install
(5/7) Installing pulseaudio-bluez (14.2-r5)
(6/7) Installing alsa-utils-openrc (1.2.4-r0)
(7/7) Installing pulseaudio-openrc (14.2-r5)
Executing busybox-1.33.0-r6.trigger
Executing dbus-1.12.20-r2.trigger
Executing glib-2.68.1-r0.trigger
OK: 663 MiB in 378 packages
```
