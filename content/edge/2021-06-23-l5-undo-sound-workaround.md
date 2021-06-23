title: "Librem 5: Action required if workaround for audio/ucm was applied"
date: 2021-06-23
---
A better workaround was identified for the issue described in a previous edge
blog post ([here](https://postmarketos.org/edge/2021/06/22/l5-no-sound/)), and
is provided in the `device-purism-librem5` package version 1.23. This update
conflicts with the workaround provided in that post.

Audio will once again stop working if `device-purism-librem5` v1.23 is
installed AND the workaround that modified `/usr/share/alsa/ucm2/ucm.conf` is
applied. To restore audio, reverse the previous workaround by re-installing
`alsa-ucm-conf`:

```
$ sudo apk fix -r alsa-ucm-conf
```

Also see:

- [pmaports!2267](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2267)
- [pmaports#1124](https://gitlab.com/postmarketOS/pmaports/-/issues/1124)
- [librem5-base #48](https://source.puri.sm/Librem5/librem5-base/-/issues/48)

