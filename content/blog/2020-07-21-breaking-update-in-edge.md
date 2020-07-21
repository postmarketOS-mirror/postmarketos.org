title: "Breaking update for 32-bit arches in postmarketOS edge"
date: 2020-07-21
---

Here is a quick announcement for postmarketOS **edge** users on the
architectures **`armhf`, `armv7` and `x86`**. Note that `aarch64` and `x86_64`
on `edge` are _not_ affected. All the architectures on the recently released
[stable channel](/blog/2020/05/31/three-years/#stable-release-channel) are also
_not_ affected.

[Alpine Linux edge is moving to a new musl libc version](https://lists.alpinelinux.org/~alpine/devel/%3C20200721171650.48fa63a4%40ncopa-desktop.copa.dup.pw%3E)
introducing 64-bit `time_t` for 32-bit architectures. This requires all
packages of the 32-bit architectures to be rebuilt against the new musl
version. In postmarketOS, we will rebuild all affected edge packages as soon as
the change is pushed to Alpine (today or tomorrow). Users will need to upgrade
as follows, as soon as packages are rebuilt in postmarketOS edge.

```shell-session
# apk upgrade -U -a
```

The build status of the postmarketOS packages can be found on
[build.postmarketos.org](https://build.postmarketos.org/). Note that the
PinePhone postmarketOS CE will be shipped with the stable channel, which does
not have such breaking changes.
