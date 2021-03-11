title: "Source Code"
---

### git repositories

Find postmarketOS related git repositories at
[https://gitlab.com/postmarketOS](https://gitlab.com/postmarketOS). Here are
the most important ones:

  * [pmaports](https://gitlab.com/postmarketOS/pmaports) holds all package
    build recipes.
    <br><small>It is similar to Alpine's [aports](https://gitlab.alpinelinux.org/alpine/aports/).</small>
  * [pmbootstrap](https://gitlab.com/postmarketOS/pmbootstrap) is the
    sophisticated chroot/build/flash tool to develop and install postmarketOS.
    <br><small>Targeted at power users and developers, for the easy way to
    install postmarketOS, see [/download](/download/).</small>
  * [linux-postmarketos](https://gitlab.com/postmarketOS/linux-postmarketos) is
    our close to mainline Linux tree
    <br><small>Device specific patches get integrated there while they are
    being [upstreamed](https://lists.sr.ht/~postmarketos/upstreaming).</small>

### Issues

Report postmarketOS specific bugs in the pmaports repository, unless they
clearly belong into another project (e.g. pmbootstrap). Upstream bugs (Alpine,
Phosh, Plasma Mobile, ...) should be reported in upstream projects. When in
doubt, rather make an issue in the
[postmarketOS tracker](https://gitlab.com/groups/postmarketOS/-/issues).


### Binary packages

If you are looking for the source code, you might also be interested in how the
packages from pmaports get transformed into the official binary packages. This
happens transparently on
[build.postmarketos.org](https://build.postmarketos.org) (bpo). Whenever a git
commit gets pushed/merged to pmaports, bpo calculates which packages need to be
rebuilt, and then builds the missing packages with pmbootstrap on
[builds.sr.ht](https://builds.sr.ht/). All build logs are publicly visible (and
can even be followed while the packages are building).

Built packages can be accessed from the
[official mirrors](https://mirrors.postmarketos.org/), and one can search
through them on
[pkgs.postmarketos.org](https://pkgs.postmarketos.org) (just like
[pkgs.alpinelinux.org](https://pkgs.alpinelinux.org)).
