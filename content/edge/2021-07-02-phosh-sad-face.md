title: "Phosh: 'Oh no!' error after recent upgrade"
date: 2021-07-02
---
A recent upgrade of `postmarketos-base-ui` to v2 has removed a XDG desktop file
for one of Phosh's dependencies, resulting in Phosh starting up to a sad face
error window with the message "Oh no! Something has gone wrong."

This can be resolved by reinstalling the package that provides the missing XDG
desktop file:

```
$ sudo apk fix -r gnome-settings-daemon
$ sudo rc-service tinydm restart
```

Also see:
- [pmaports#1140](https://gitlab.com/postmarketOS/pmaports/-/issues/1140)
