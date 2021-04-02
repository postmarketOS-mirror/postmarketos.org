title: "pulseaudio removed by pipewire-pulse-0.3.24-r1"
date: 2021-04-02
---
A recent update on edge caused the `pipewire-pulse` package to completely
replace `pulseaudio`. This was not intended, and resulted in broken audio on
some devices.

The upstream package has been fixed. In order to apply the fix to a system
which received the `pipewire-pulse-0.3.24-r1` upgrade, perform the following
steps:

```
$ sudo apk update
$ sudo apk add !pipewire-pulse
$ sudo reboot
```

You should see that `pipewire-pulse` was removed and `pulseaudio` was
re-installed. If this did not happen, please let us know.

If your system did not receive `pipewire-pulse-0.3.24-r1`, continue to upgrade
your system normally.
