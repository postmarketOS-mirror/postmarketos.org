title: "PinePhone CE\navailable for pre-order"
date: 2020-07-15
---

## Introduction
[#grid side#]
[![](/static/img/2020-07/pinephone-postmarketos-ce-front-thumb.png)](/static/img/2020-07/pinephone-postmarketos-ce-front.png)
[#grid text#]
This is a follow-up to last month's
[PinePhone: postmarketOS community edition](/blog/2020/06/15/pinephone-postmarketos-community-edition/)
announcement. PINE64 and postmarketOS are teaming up to bring you the next
version of this remarkable, hacker-friendly smartphone.
[Pre-orders are open now.](https://store.pine64.org/product-category/pinephone/) Keep in mind, that you
should only buy this device if you
[consider yourself a Linux enthusiast](/blog/2020/06/15/pinephone-postmarketos-community-edition/#linux-enthusiasts-only).

## Hardware news
We are happy to share that in addition to the [standard PinePhone CE hardware
configuration](/blog/2020/06/15/pinephone-postmarketos-community-edition/#the-pinephone),
the postmarketOS CE can be ordered in an all-new Convergence Package. It comes
with increased RAM (3 GB instead of 2 GB), eMMC (32 GB instead of 16 GB) and
price ($199.99 instead of $149.99), as well as the nice USB-C dock seen in the
picture.
[#grid end#]

[#grid side#]
[![](/static/img/2020-07/pinephone-dock-thumb.png)](/static/img/2020-07/pinephone-dock.jpg)
[#grid text#]
<br>
With USB-C power-in, HDMI, Ethernet and two USB ports, there is much potential
to turn your phone
[into something like a desktop computer](https://www.youtube.com/watch?v=yBeza4UNOm8).
(Beta reminder: while already way more convenient than
[this setup](/static/img/2019-06/hammerhead-convergence.jpg), convergence needs
more work on the software side.)
[#grid end#]

Furthermore, the PinePhone postmarketOS CE will have a fix for a design flaw
present in earlier revisions of the PinePhone. In the much appreciated spirit
of sustainability, PINE64 explains how owners of previous revisions will be
able to get it fixed. More about that and other hardware details are in today's
[PINE64 announcement](https://www.pine64.org/2020/07/15/july-update:pmos-ce-pre-orders-and-new-pinephone-version/).

## Software news
Several fixes and improvements were made in postmarketOS, that relate to the
PinePhone (thanks to
[@Cogitri](https://gitlab.com/Cogitri),
[@Danct12](https://gitlab.com/Danct12),
[@DolphinChips](https://gitlab.com/DolphinChips),
[@ell1e](https://gitlab.com/ell1e),
[@MartijnBraam](https://gitlab.com/MartijnBraam),
[@megi](https://xnux.eu/devices/pine64-pinephone.html),
[@ollieparanoid](https://gitlab.com/ollieparanoid),
[@PureTryOut](https://gitlab.com/PureTryOut)). Most importantly, phone calls
[with audio](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1412)
are fixed on the stable channel. Shout out to [@a-wai](https://gitlab.com/a-wai)
from [Mobian](https://mobian-project.org/) for developing a workaround to let
Phosh switch the audio channel for calls, we
[packaged](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1406) this
patch for now.

<div style="text-align: center">
<a href="/static/img/2020-07/phosh-firefox.png"><img
	src="/static/img/2020-07/phosh-firefox-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-07/phosh-gnome-software.png"><img
	src="/static/img/2020-07/phosh-gnome-software-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-07/phosh-pulldown-menu.png"><img
	src="/static/img/2020-07/phosh-pulldown-menu-thumb.jpg" class="w150 border"></a>
</div>

GNOME software and other applications have gotten
Purism's [mobile UI patches](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1346)
on the stable channel. Together with the
[blazingly fast](https://michael.stapelberg.ch/posts/2019-08-17-linux-package-managers-are-slow/)
package manager from Alpine Linux, this gives a convenient method of installing
updates with a touch UI in a matter of seconds. Firefox gets
[scaled](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1396) to fit
the mobile screen (making it pretty usable) and the Epiphany browser has gotten
a [privacy friendly user-agent](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1402).

### Installer with optional SSH server and encryption

The postmarketOS
[on-device installer](https://wiki.postmarketos.org/wiki/On-device_installer)
has been extended to not only ask for the LUKS full disk encryption password
(which we find absolutely essential). But also to allow setting the lockscreen
PIN and to enable an SSH server. The SSH login would be very weak if we just
used the default user with the lockscreen PIN as password, so we have disabled
that in `sshd_config` and ask for a second set of credentials instead. People
are even encouraged to disable password login completely and install an SSH
key when using the SSH server for the first time.

<div style="text-align: center">
<a href="/static/img/2020-07/ondev-welcome.png"><img
	src="/static/img/2020-07/ondev-welcome-thumb.jpg" class="w150 border"></a>

<a href="/static/img/2020-07/ondev-user-pin.png"><img
	src="/static/img/2020-07/ondev-user-pin-thumb.jpg" class="w150 border"></a>

<a href="/static/img/2020-07/ondev-ssh-confirm.png"><img
	src="/static/img/2020-07/ondev-ssh-confirm-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-07/ondev-ssh-credentials.png"><img
	src="/static/img/2020-07/ondev-ssh-credentials-thumb.jpg" class="w150 border"></a>

<a href="/static/img/2020-07/ondev-fde.png"><img
	src="/static/img/2020-07/ondev-fde-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-07/ondev-fde-pass.png"><img
	src="/static/img/2020-07/ondev-fde-pass-thumb.jpg" class="w150 border"></a>
</div>

This installer is slowly shaping into a blend of a typical, powerful Linux
distribution installer with an intuitive (even for non-tech people) user
interface that is suitable for mobile devices. Below the surface, we are
using [Calamares](https://calamares.io), which is already widely used as
installer among desktop Linux distributions. We plan to
[upstream](https://github.com/calamares/calamares/issues/1451) our [custom
modules](https://gitlab.com/postmarketOS/postmarketos-ondev/) into the main
Calamares repository, so other mobile-centric Linux distributions can use and
improve them too. Thanks to
[@adriaandegroot](https://gitlab.com/adriaandegroot) for quickly fixing several
bugs in Calamares related to these efforts.

## Pre-order now!

If you like what you see here, there's no time like the present to [head over
to the PINE64 shop and order your PinePhone postmarketOS community edition](https://store.pine64.org/product-category/pinephone/).

## Comments

* [Reddit](https://www.reddit.com/r/postmarketOS/duplicates/hrpmkk/postmarketos_pinephone_ce_available_for_preorder/)
* [HN](https://news.ycombinator.com/item?id=23846588)
