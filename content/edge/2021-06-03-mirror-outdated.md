title: "Alpine Linux dl-2 mirror is currently outdated"
date: 2021-06-03
---

As of writing, the mirror dl-2.alpinelinux.org is outdated by four days for
Alpine edge, on which postmarketOS edge is based. It is up to date for v3.12,
on which our latest release, v21.03 is based.

Find the current mirror status on
[mirrors.alpinelinux.org](https://mirrors.alpinelinux.org/).

If you are affected by this, you can change your mirror to another one
(e.g. `dl-cdn.alpinelinux.org`) by editing `/etc/apk/repositories`.

Related issue:
[build.postmarketos.org#101](https://gitlab.com/postmarketOS/build.postmarketos.org/-/issues/101)
