title: "Missing armv7 packages"
date: 2021-04-18
---
Due to
[bpo#98](https://gitlab.com/postmarketOS/build.postmarketos.org/-/issues/98),
lots of armv7 packages are missing in the postmarketOS edge binary repository.
Rebuilding is in progress, find the status at
[build.postmarketos.org](https://build.postmarketos.org).

If you need to install missing armv7 packages from postmarketOS on an existing
edge install, consider building them with pmbootstrap and
[making your local repository available over network](https://wiki.postmarketos.org/wiki/Installing_packages_on_a_running_phone).

For new installs, pmbootstrap will build missing packages if you enable the
following option at the end of `pmbootstrap init`:

```
After pmaports are changed, the binary packages may be outdated. If you want to install postmarketOS without changes, reply 'n' for a faster installation.
Build outdated packages during 'pmbootstrap install'? (y/n) [y]:
```

