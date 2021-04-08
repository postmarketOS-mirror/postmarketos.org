title: "Python 3.9 / protobuf temporarily removed for 32-bit arches / qt5-qtsvg error"
date: 2021-04-08
---

## Python 3.9

Python has been upgraded from 3.8 to 3.9 in Alpine. All packages currently
depending on libpython3.8.so or installing files to /usr/lib/python3.8/ need
to be rebuilt. The former causes errors while trying to install python packages
and the latter causes errors like the following at runtime:

> ModuleNotFoundError: No module named 'gpodder'

Relevant links:

* postmarketOS fixes: [pmaports!2104](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2104)
* Alpine fixes: see
[open and closed MRs mentioning python](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests?scope=all&utf8=%E2%9C%93&state=opened&search=python).
* [Alpine package search](https://pkgs.alpinelinux.org/contents?file=&path=%2Fusr%2Flib%2Fpython3.8%2F*&name=*&branch=edge)
  with packages that still need to be adjusted (note that this has a delay, the
  search results aren't directly updated after a merge)
* Consider helping out with fixing the remaining packages in Alpine, if there
  isn't a merge request already (open or merged)

## protobuf

Protobuf was briefly disabled in Alpine for 32-bit arches. Plasma Mobile and
Phosh both depend on this package through libphonenumber. It is
[enabled again.](https://gitlab.alpinelinux.org/alpine/aports/-/commit/94bd1b9446f8e59d3e69a9844b65b27023207c02)

## qt5-qtsvg

A broken patch in qt5-qtsvg caused build errors like the following. The patch
has been
[reverted](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/20307)
in Alpine (the fixed package was also
[forked](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/2104)
to postmarketOS, so we could get the upstream compatibility issues fixed all at
once without waiting until it was built and published in Alpine).

```
CMake Error at /usr/lib/cmake/Qt5Svg/Qt5SvgConfig.cmake:111 (find_package):
  Could not find a configuration file for package "Qt5Widgets" that is
  compatible with requested version "5.15.3".
  The following configuration files were considered but not accepted:
    /usr/lib/cmake/Qt5Widgets/Qt5WidgetsConfig.cmake, version: 5.15.2
```
