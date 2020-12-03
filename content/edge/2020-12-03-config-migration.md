title: "postmarketos-base: config migration"
date: 2020-12-03
---

Logic in the postmarketos-base package was changed to properly overwrite config
files from Alpine. The old config files get automatically moved to
/etc/postmarketos-mvcfg/backup, just in case they were modified by the user.
Details are in the
[wiki page](https://wiki.postmarketos.org/wiki/Packaging:_Override_Configuration_Files).
