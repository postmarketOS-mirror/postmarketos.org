title: "pipewire-pulse used instead of pipewire in new pmbootstrap installs"
date: 2021-04-15
---
When building postmarketOS images with the Phosh UI, pipewire-pulse gets
installed instead of pulseaudio. This results in broken audio.

Existing installs and pre-built images are not affected.

More information: [#1067](https://gitlab.com/postmarketOS/pmaports/-/issues/1067)
