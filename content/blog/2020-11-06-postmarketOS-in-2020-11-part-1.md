title: "postmarketOS in 2020-11: Apps, UIs & Devices"
date: 2020-11-06
---

After a several month hiatus in blog posts, we're back to give you, our dear
readers, an update on what has been happening in postmarketOS development land
since our last post. It's quite a lot, and we do not want to leave out any
juicy details, so to make it easier to digest we'll be splitting this update
post into a two part series. Welcome to part 1!

## Apps
### Megapixels
[#grid side#]
[![](/static/img/2020-11/megapixels-thumb.png){: class="w300"}](/static/img/2020-11/megapixels.png)
[#grid text#]
Once camera drivers for your phone have been written and land in the Linux
kernel, you might assume that you can just use any existing camera program on
Linux to take some beautiful photos. But far from it!

Pretty much all of today's camera apps in the Linux world are built on top of
the GStreamer framework (either directly or indirectly). GStreamer is not yet
able to deal with subdevices and media graphs exposed by the V4L2 API in the
kernel. [@MartijnBraam](https://gitlab.com/MartijnBraam) would like to extend
GStreamer eventually to make all apps using it work out of the box. But he also
realized that it is a big undertaking and decided to write the simplistic GTK+3
app [Megapixels](https://git.sr.ht/~martijnbraam/megapixels), which directly
talks to V4L2 without GStreamer. It uses device specific config files (shipped
with the source) instead of trying to do complex automatic configuration, and
comes with a mobile interface. Martijn's first target was of course the
PinePhone, but this is just the start. From the latest rendition of his
[epic](https://blog.brixit.nl/camera-on-the-pinephone/)
[camera](https://blog.brixit.nl/pinephone-camera-part-2/)
[blog](https://blog.brixit.nl/pinephone-camera-adventures-part-3/)
[posts](https://blog.brixit.nl/pinephone-camera-pt4/):
[#grid end#]

> I think with these changes the ov5640 is basically stretched to the limit of
what's possible with the photo quality. The rest of the planned tasks is mainly
UX improvement and supporting more different camera pipelines. Since
postmarketOS supports a lot of phones and more and more run mainline Linux it
should be possible to also run Megapixels on some of those.

Needless to say, we've made this app the default in `postmarketos-ui-phosh`.
Beyond that, it made its way into the distributions from our friends at
[Arch Linux ARM](https://github.com/dreemurrs-embedded/Pine64-Arch/),
[Manjaro](https://manjaro.org/)
and [Mobian](https://mobian-project.org/).

<small>
*Thanks to:
[@MartijnBraam](https://gitlab.com/MartijnBraam)
*
</small>

### Firefox
[#grid side#]
[![](/static/img/2020-11/mobile-config-firefox-thumb.jpg){: class="w300 border"}](/static/img/2020-11/mobile-config-firefox.png)
[#grid text#]
With a few config tweaks, the desktop version of Firefox 68 would work
surprisingly well on mobile devices. Unfortunately this is not so much the
case for later versions, and 68 was about to hit End of Life.
[@ollieparanoid](https://gitlab.com/ollieparanoid) stepped in and tweaked our
config in multiple iterations, the final one being the distro-independent
[mobile-config-firefox](https://gitlab.com/postmarketOS/mobile-config-firefox/)
repository with CSS UI tweaks created by using Firefox' own
[remote debugger](https://gitlab.com/postmarketOS/mobile-config-firefox/#contributing-changes-to-userchrome).
Besides making the UI fit the screen, the configs disables some clutter (e.g.
first run page, post update page, "user messaging") and apply privacy tweaks
(e.g. not sending search queries as you type to search engines). Furthermore it
comes with a lightweight start page (pulled from your local install, not from
the Internet), which provides a convenient link to install the privacy
enhancing and performance/battery saving content blocker
[uBlock Origin](https://github.com/gorhill/uBlock/). If you don't like these
defaults, you could of course change the settings as you like or remove the
`mobile-config-firefox` package altogether.
[#grid end#]

Just like Megapixels, this config is used by other distributions too.
[@a-wai](https://gitlab.com/a-wai) from Mobian contributed
[!2](https://gitlab.com/postmarketOS/mobile-config-firefox/-/merge_requests/2)
to tweak the installation of the custom CSS file.

<small>
*Thanks to:
[@a-wai](https://gitlab.com/a-wai),
[@ollieparanoid](https://gitlab.com/ollieparanoid)
*
</small>

### osk-sdl
Our full disk encryption initramfs keyboard
[osk-sdl](https://gitlab.com/postmarketOS/osk-sdl) is about to receive a major
performance improvement
([!1557](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1557)), as
we will be able to use GPU acceleration. Also the code has been cleaned up
([!92](https://gitlab.com/postmarketOS/osk-sdl/-/merge_requests/92),
[!95](https://gitlab.com/postmarketOS/osk-sdl/-/merge_requests/95)). The
initramfs gets rebuilt with each osk-sdl upgrade now, not only with kernel
upgrades
([!1563](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1563)).

<small>
*Thanks to:
[@craftyguy](https://gitlab.com/craftyguy),
[@minlexx](https://gitlab.com/minlexx),
[@PureTryOut](https://gitlab.com/PureTryOut),
[@wczyz](https://gitlab.com/wczyz),
[@z3ntu](https://gitlab.com/z3ntu)
*
</small>

## User Interfaces
### Phosh
[#grid side#]
[![](/static/img/2020-11/phosh-0.5.0-thumb.jpg){: class="w200 border"}](/static/img/2020-11/phosh-0.5.0.png)
[#grid text#]
Phosh was upgraded to the latest version 0.5.1
([!1623](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1623),
[!1656](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1656),
[!1680](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1680)). Most
noticeable are the new *Torch* and *Undocked* buttons in the top panel. You
guessed right, the *Torch* allows you to see in the dark. *Undocked* indicates
whether your phone is connected to a dock, that is, if there are more than one
screen and a mouse attached. Then it will say *Docked* and the window handling
of Phosh becomes more desktop-friendly.

Regarding default apps, we have added Megapixels as mentioned above, the image
viewer [eog](https://wiki.gnome.org/Apps/EyeOfGnome/) and the file manager
[Nemo](https://github.com/linuxmint/nemo). Eog gets started from Nemo or
Megapixels when trying to open an image file.

<small>
*Thanks to:
[@afontain](https://gitlab.com/afontain),
[@Cogitri](https://gitlab.com/Cogitri),
[@craftyguy](https://gitlab.com/craftyguy),
[@guido.gunther](https://source.puri.sm/guido.gunther),
[@MartijnBraam](https://gitlab.com/MartijnBraam),
[@ollieparanoid](https://gitlab.com/ollieparanoid),
[@TimotheeLF](https://gitlab.com/TimotheeLF),
[@z3ntu](https://gitlab.com/z3ntu)
*
</small>
[#grid end#]

### Plasma
[#grid side#]
[![](/static/img/2020-11/plasma-mobile-thumb.jpg){: class="w200 border"}](/static/img/2020-11/plasma-mobile.jpg)
[#grid text#]
[Plasma Mobile](https://www.plasma-mobile.org/) was upgraded by
[@PureTryOut](https://gitlab.com/PureTryOut)
to the latest version as well, which is based on KDE Plasma 5.20.1
([!1590](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1590)).
Among other changes, the homescreen has been redesigned. The
icons at the bottom and the search bar aren't on a solid background anymore,
just directly on the wallpaper. In
[!1643](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1643), the
[Peruse](https://invent.kde.org/graphics/peruse) comic book reader app has
been packaged by [@z3ntu](https://gitlab.com/z3ntu).

[@PureTryOut](https://gitlab.com/PureTryOut) also did the initial packaging of
[Plasma Bigscreen](https://plasma-bigscreen.org/)
([!1522](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1552)). This
interface was made for TVs and could be used in the future if we start to
replace abandoned smart TV software with postmarketOS. And of course today if
you throw it on something like a Raspberry Pi or RockPro64 and connect that to
your big monitor.

<small>
*Thanks to:
[@bshah](https://gitlab.com/bshah),
[@PureTryOut](https://gitlab.com/PureTryOut),
[@z3ntu](https://gitlab.com/z3ntu)
*
</small>
[#grid end#]

### Sxmo
[#grid side#]
<video controls width="200" height="356" autoplay="autoplay" class="border" loop>
<source src="/static/video/2020-11/sxmo-thumb.webm" />
</video>
<br>
<span class="w200">
Sxmo in action. ([bigger](/static/video/2020-11/sxmo.webm))
</span>
[#grid text#]
[@milesalan](https://gitlab.com/milesalan) contributed the packages of
[Sxmo](https://sr.ht/~mil/Sxmo/) into the postmarketOS pmaports repository
([!1472](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1472)):
> Sxmo, or Simple X Mobile, is a collection of simple and
[suckless](https://suckless.org/) X programs and scripts used together to
create a fully functional mobile UI adhering to the
[Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) for the
[PinePhone](https://www.pine64.org/pinephone/). You control the UI largely
through using the PinePhone buttons (press different numbers of times quickly
for different actions) and swipe gestures.

The project started as downstream project from postmarketOS, with PinePhone
specific images. Now that the packages have been upstreamed, it is possible to
install the UI not just on the PinePhone, but in theory on most of the phones
that run postmarketOS.
[#grid end#]

<small>
*Thanks to:
[@milesalan](https://gitlab.com/milesalan)
*
</small>

### Shelli
[@unrznbl](https://gitlab.com/unrznbl)'s TTY interface Shelli
([introduced here](/blog/2019/06/23/two-years/#shelli)) is at version 0.5.0
now
([!1354](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1354)). It
features much better dynamic device path detection: power button, touch
screen and brightness should all work on most devices. Moreover the new release
brings good oFono integration with modem for SMS and voice. With all the
modem related additions, the only thing missing for basic phone operations with
Shelli is data and MMS.

> Speaking of MMS. I will be working on integrating mmsd from the oFono project
with Shelli. I hope this will help other UIs achieve good MMS support.
See [mms-stack](https://sr.ht/~anteater/mms-stack/) for a good resource on the
various ways MMS can be worked on. Help out!

Find more details
on what works and which commands are present in the
[source tree](https://gitlab.com/unrznbl/shelli/-/tree/v0.5).

<small>
*Thanks to:
[@unrznbl](https://gitlab.com/unrznbl)
*
</small>

## Devices
### (Close to) Mainline
#### PinePhone and PineTab

For all the Linux enthusiasts who bought a PineTab or PinePhone (our own
[pmOS CE](/blog/2020/07/15/pinephone-ce-preorder/) is sold out, but as of
writing, the next iteration with Manjaro is
[in stock](https://pine64.com/product-category/pinephone/)): we generated a
[new set of images](https://images.postmarketos.org) and have exciting
improvements to cover.

[#grid side#]
[![](/static/img/2020-11/pinephone-ce-with-box-thumb.jpg){: class="w300 border"}](/static/img/2020-11/pinephone-ce-with-box.png)
<br>
<span class="w300">
The postmarketOS CE came with pmbootstrap source all over the box.
</span>
[#grid text#]
##### Megi's tree and HDMI fix

The `linux-postmarketos-allwinner` kernel that both devices use is now
following [@megi](https://xnux.eu)'s 5.9.x based
[source tree](https://megous.com/git/linux/)
([!1614](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1614)). He
drives the PinePhone related kernel development forward like no other. Not only
with his own patches, but also by having a sane tree that integrates relevant
changes from other developers until they are upstreamed. Changes are easy to
follow in his [log](https://xnux.eu/log) and he makes frequent release tags
when there is something worth packaging. This simplifies our workflow a lot,
and by only carrying the few pmOS specific patches in
[pmaports](https://gitlab.com/postmarketOS/pmaports/-/tree/master/main/linux-postmarketos-allwinner)
(instead of an own git tree with mostly the same patches), it is easier to see
where we deviate from this tree. We get a much quicker and more reliable
workflow of upgrading the kernel and bug reports become more useful.
[#grid end#]

Such as the report that external HDMI was not working with most displays in a
stock postmarketOS install
([#735](https://gitlab.com/postmarketOS/pmaports/-/issues/735)), although it
worked when selecting postmarketOS in [@megi](https://xnux.eu/)'s own
[multi-distro demo image](https://xnux.eu/p-boot-demo/).
[@ollieparanoid](https://gitlab.com/ollieparanoid) spent a day building kernels
with different configs and patches, [@bshah](https://gitlab.com/bshah) went
through related kernel code line by line in both trees. Only after using
the exact same kernel, we realized that the special bootloader
[p-boot](https://xnux.eu/p-boot/) made the difference. [@megi](https://xnux.eu)
[analyzed it further](https://xnux.eu/log/#021) and fixed the bug in the
kernel.

##### List of improvements

Besides the HDMI fix, the most notable improvements for the PINE64 devices in
postmarketOS are:

* [60 FPS display framerate fix](https://xnux.eu/log/#023)
  ([!1661](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1661))
* [Better quality for incoming calls](https://xnux.eu/log/#020)
* [Fix "high-pitched whine" from the speaker on boot](https://xnux.eu/log/#020)
* Fix excessive mic noise on call
  ([!1652](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1652))
* Front and back camera working, with autofocus
  ([!1654](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1654))
* Fix suspend
  ([!1636](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1636),
  [!1651](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1651))
* Encrypted installs: allow unlock with keyboard
  ([!1555](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1555))
* Fix [USB network](https://wiki.postmarketos.org/wiki/USB_Network)
  ([#687](https://gitlab.com/postmarketOS/pmaports/-/issues/687))

##### PineTab: Early Adopters edition
Support for the new display panel of the PineTab Early Adopters edition was
added
([!1627](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1627)). By
asking for the version after selecting the PineTab in `pmbootstrap init`,
postmarketOS works with both the new version and the previous
[pinetab-dev](https://wiki.pine64.org/index.php?title=PineTab#Versions).

<small>
*Thanks to:
[@bshah](https://gitlab.com/bshah),
[@craftyguy](https://gitlab.com/craftyguy),
[@djselbeck](https://gitlab.com/djselbeck),
[@MartijnBraam](https://gitlab.com/MartijnBraam),
[@megi](https://xnux.eu),
[@ollieparanoid](https://gitlab.com/ollieparanoid),
[@pedromoreno](https://gitlab.com/pedromoreno),
[@PureTryOut](https://gitlab.com/PureTryOut),
[@smaeul](https://gitlab.com/smaeul),
[@tmlind](https://github.com/tmlind),
[@z3ntu](https://gitlab.com/z3ntu)
*
</small>

### Librem 5
[#grid side#]
[![](/static/img/2020-11/librem5-chatty-thumb.jpg){: class="w200 border"}](/static/img/2020-11/librem5-chatty.jpg)

[![](/static/img/2020-11/librem5-dev-openmw-thumb.jpg){: class="w200 border"}](/static/img/2020-11/librem5-dev-openmw.jpg)
[#grid text#]
[@craftyguy](https://gitlab.com/craftyguy) keeps on upgrading and testing the
Linux kernel and device configs provided by Purism for their Librem 5 phone
with postmarketOS. In a guest post on the Purism blog, he describes his
[Adventures of porting postmarketOS to the Librem 5](https://puri.sm/posts/adventures-of-porting-postmarketos-to-the-librem-5/). One of the gems:

> A lot of folks in the Purism Matrix channels are excited about “device
convergence,” in particular using your phone with an external
keyboard/mouse/monitor as you would a desktop PC. Not to be the one left out,
I thought it might be fun to play Elder Scrolls 3: Morrowind (via
[OpenMW](https://openmw.org/en/)), which basically requires a keyboard/mouse to
use. After packaging OpenMW in Alpine Linux, I was now able to play one of the
best RPGs ever made on the devkit. Albeit, not at a super smooth frame rate,
but that was to be expected given how early this hardware was and the current
state of its support in Mesa.

<small>
*Thanks to:
[@craftyguy](https://gitlab.com/craftyguy)
*
</small>
[#grid end#]

#### Modem

[@Minecrell](https://gitlab.com/Minecrell) wrote a shiny new
[BAM DMUX](https://github.com/msm8916-mainline/linux/pull/103) kernel
driver:

> This adds a new, (imo) mainline-quality driver for the BAM DMUX interface
that provides the network interface to the modem on MSM8916 and MSM8974. It
replaces the old 20k+ driver I ported from downstream a while ago.
>
> I spent almost the entire last week to write it from scratch. It lacks some
performance optimizations of the downstream driver but otherwise it has much
better code quality. Overall it seems to work just fine.

Additionally he wrote ModemManager patches to talk to the modem via rpmsg
channels, so they can make use of this new driver
([!1607](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1607)). The
merge request also contains reports about how this can be used with Dual SIM
phones. All in all, his work makes voice calls, SMS and mobile data for both
SoCs possible - with both oFono and with ModemManager!

[@akulichalexander](https://gitlab.com/akulichalexander) fixed outgoing calls
in the oFono QMI modem driver
([!1637](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1637)).

<small>
*Thanks to:
[@akulichalexander](https://gitlab.com/akulichalexander),
[@aleksander0m](https://gitlab.com/aleksander0m),
[@Minecrell](https://gitlab.com/Minecrell),
[@minlexx](https://gitlab.com/minlexx),
[@srxl](https://gitlab.com/srxl),
[@TravMurav](https://gitlab.com/TravMurav),
[@z3ntu](https://gitlab.com/z3ntu)
*
</small>


#### Mainline all the phones and tablets!
The
[Samsung Galaxy SII](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_SII_(samsung-i9100))
can run on a mainline kernel now
([!1598](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1598)) and
we have ongoing work to create a new shared
`linux-postmarketos-exynos4` kernel for the SII and SIII / SIII LTE
([!1634](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1634)).

[#grid side#]
[![](/static/img/2020-11/samsung-i9100-mainline-thumb.jpg){: class="w200 border"}](/static/img/2020-11/samsung-i9100-mainline.jpg)
<br>
<span class="w200">
The Samsung Galaxy SII running mainline, one of the two phones where
<a href="/blog/2017/05/26/intro/">it all began</a> in 2017.
</span>

[#grid text#]
The shared
[MSM8916](https://wiki.postmarketos.org/wiki/Qualcomm_Snapdragon_410/412_(MSM8916))
packaging got a major update in
([!1603](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1603)). Its
kernel was rebased onto 5.9-rc7, had major device tree rewrites and code
cleanup. Besides that, the update brought the BAM DMUX driver mentioned above,
as well as improved or initial support for the following devices (refer to the
merge request for details):

* [BQ Aquaris X5](https://wiki.postmarketos.org/wiki/BQ_Aquaris_X5_(bq-picmt/paella))
* [Motorola Moto E 2015](https://wiki.postmarketos.org/wiki/Motorola_Moto_E_2015_(motorola-surnia)) (new)
* [Oppo Mirror 5s](https://wiki.postmarketos.org/wiki/Oppo_Mirror5s_(oppo-a51f)) (new)
* [Samsung Galaxy A3 (2015)](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_A3_2015_(samsung-a3ulte))
* [Samsung Galaxy A5 (2015)](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_A5_2015_(samsung-a5ulte))
* [Samsung Galaxy Grand Prime](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_Grand_Prime_CAN_(samsung-gprimeltecan)) (new)
* [Samsung Galaxy J5 2015](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_J5_2015_(samsung-j5nlte))
* [Xiaomi Redmi 2](https://wiki.postmarketos.org/wiki/Xiaomi_Redmi_2_(xiaomi-wt88047)) (new)
[#grid end#]


[MSM8953](https://wiki.postmarketos.org/wiki/Qualcomm_Snapdragon_450/625/626/632_(MSM8953))
has gotten similar shared kernel packaging, and is initially being used by the
[Motorola Moto G7 Power](https://wiki.postmarketos.org/wiki/Motorola_Moto_G7_Power_(motorola-ocean))
([!1558](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1558)). The
[MSM8974](https://wiki.postmarketos.org/wiki/Qualcomm_Snapdragon_800/801_(MSM8974))
kernel was upgraded to 5.9
([!1572](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1572)) and
it is now being used for the mainline port of the 
[Xperia Z2 Tablet LTE](https://wiki.postmarketos.org/wiki/Sony_Xperia_Z2_Tablet_LTE_(sony-castor)).
Likewise, the
[(close to) mainline](https://wiki.postmarketos.org/wiki/(Close_to)_Mainline)
kernel of the
[OnePlus 6/6T](https://wiki.postmarketos.org/wiki/OnePlus_6_(oneplus-enchilada))
was upgraded to 5.9 and got preparations for audio support
([!1653](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1635)).

What's more, the
[Google Nexus 7 2012](https://wiki.postmarketos.org/wiki/Google_Nexus_7_2012_(asus-grouper))
tablet has gotten support for the older PM269 variant
([!1532](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1532)) and
its kernel was upgraded to 5.9 as well
([!1528](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1528)). A
port for the single board computer
[Cubietech Cubieboard](https://wiki.postmarketos.org/wiki/Cubietech_Cubieboard_(cubietech-cubieboard))
was added, and due to the great
existing upstream support, it can directly use `linux-edge` from Alpine Linux
([!1589](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1589)).

<small>
*Thanks to:
@aka_,
[@calebccff](https://gitlab.com/calebccff),
[@DolphinChips](https://gitlab.com/DolphinChips),
[@ichernev](https://gitlab.com/ichernev),
[@julianuu](https://gitlab.com/julianuu),
[@krzk](https://github.com/krzk),
[@lazzardo](https://gitlab.com/lazzardo),
[@Minecrell](https://gitlab.com/Minecrell),
[@minlexx](https://gitlab.com/minlexx),
[@Mis012](https://gitlab.com/Mis012),
[@mszyprow](https://github.com/mszyprow),
[@natsu1978](https://gitlab.com/natsu1978)
[@nergzd723](https://gitlab.com/nergzd723),
[@NotJunak](https://gitlab.com/NotJunak),
[@plata-gl](https://gitlab.com/plata-gl),
[@Sekilsgs2](https://github.com/Sekilsgs2),
[@symmetrist](https://gitlab.com/symmetrist),
[@ThiagaoPlusPlus](https://gitlab.com/ThiagaoPlusPlus),
[@timbz](https://gitlab.com/timbz),
[@TravMurav](https://gitlab.com/TravMurav),
[@Ultracoolguy](https://gitlab.com/Ultracoolguy),
[@unrznbl](https://gitlab.com/unrznbl),
[@wiktorek140](https://gitlab.com/wiktorek140),
[@WTechNinja](https://gitlab.com/WTechNinja)
*
</small>

#### Various device changes

[![](/static/img/2020-11/nokia-n900-keymap-se.jpg){: class="border center"}](/static/img/2020-11/nokia-n900-keymap-se.jpg)

<span class="img-center-subtext">
How the N900 keyboard looks like in Finland and Sweden.
</span>

[Nokia N900](https://wiki.postmarketos.org/wiki/Nokia_N900_(nokia-n900))
users get support for Finnish and Swedish keymaps by
[@linusw](https://gitlab.com/linusw)
([!1519](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1519))
and
[@antoni.aloytorrens](https://gitlab.com/antoni.aloytorrens) made Wi-Fi work
with the
[ASUS Eee Pad Transformer](https://wiki.postmarketos.org/wiki/ASUS_Eee_Pad_Transformer_(asus-tf101))
([!1534](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1534)).

The GCC-10 upgrade caused build failures for lots of kernels in our
repositories. [@z3ntu](https://gitlab.com/z3ntu) applied the small but now
required patch to ~100 kernels that needed it, made sure all of our kernels are
still building and fixed those that didn't
([!1684](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1684)).

In addition to the mainline related modem work,
[@Minecrell](https://gitlab.com/Minecrell) also made the downstream kernels
work with modem again
([!1640](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1640)). This
is useful to debug features that are broken in mainline, but work on
downstream.

<small>
*Thanks to:
[@afontain](https://gitlab.com/afontain),
[@antoni.aloytorrens](https://gitlab.com/antoni.aloytorrens),
[@dsankouski](https://gitlab.com/dsankouski),
[@HenriDellal](https://gitlab.com/HenriDellal),
[@linusw](https://gitlab.com/linusw),
[@M0Rf30](https://gitlab.com/M0Rf30),
[@rmcgu](https://gitlab.com/rmcgu),
[@ThiagaoPlusPlus](https://gitlab.com/ThiagaoPlusPlus),
[@undevdecatos](https://gitlab.com/undevdecatos)
*
</small>



### New device ports
In the last six months, the following devices were added to postmarketOS. As
always, the ports range from barely booting with a downstream kernel to running
fairly well on (close to) mainline. For categorization by usability, see the
[wiki](https://wiki.postmarketos.org/wiki/Devices).
[#grid side#]
[![](/static/img/2020-11/samsung-skomer-plamo-thumb.jpg){: class="w200 border"}](/static/img/2020-11/samsung-skomer-plamo.jpg)
<br>
<span class="w200">
Plasma Mobile on the Samsung Galaxy Xcover 2, with (close to) mainline kernel.
</span>

[![](/static/img/2020-11/xiaomi-ferrari-weston-thumb.jpg){: class="w200 border"}](/static/img/2020-11/xiaomi-ferrari-weston.jpg)
<br>
<span class="w200">
Weston on the fresh<br>
Xiaomi Mi 4i port.
</span>

[![](/static/img/2020-11/motorola-nash-thumb.jpg){: class="w200 border"}](/static/img/2020-11/motorola-nash.jpg)
<br>
<span class="w200">
XFCE4 rocking the Motorola Moto Z2 Force, with neofetch in the terminal.
</span>
[#grid text#]

<!-- Generated with: 'pmos-stats new-devices --md 995af7fb7208c73e0d38d8e4229a4afb049c2540'
     Start subject: kde/plasmatube: new aport (MR 1157)
     Current master (for next time): 81f8ca8e776eaa0d82df418a46a2d30e3832ce18
     Current subject: device/testing/linux-*: get building again (MR 1684) -->

* [Acer Iconia Tab A500](https://wiki.postmarketos.org/wiki/Acer Iconia Tab A500 (acer-picasso))
* [Amazon Fire HD 8 (2017)](https://wiki.postmarketos.org/wiki/Amazon Fire HD 8 2017 (amazon-douglas))
* [Amazon Fire 7 (2019)](https://wiki.postmarketos.org/wiki/Amazon Fire 7 2019 (amazon-mustang))
* [Arrow DragonBoard 410c](https://wiki.postmarketos.org/wiki/Arrow DragonBoard 410c (arrow-db410c))
* [Cubietech Cubieboard](https://wiki.postmarketos.org/wiki/Cubietech Cubieboard (cubietech-cubieboard))
* [Essential PH1](https://wiki.postmarketos.org/wiki/Essential Phone (essential-mata))
* [Fly Spark](https://wiki.postmarketos.org/wiki/Fly Spark (fly-iq4404))
* [HTC One X+](https://wiki.postmarketos.org/wiki/HTC One X+ (htc-endeavor-c2))
* [HTC HD2](https://wiki.postmarketos.org/wiki/HTC HD2 (htc-leo))
* [Huawei P8 Lite](https://wiki.postmarketos.org/wiki/Huawei P8 Lite (huawei-alice))
* [Motorola Moto Z Play](https://wiki.postmarketos.org/wiki/Motorola Z Play (motorola-addison))
* [Motorola Moto Z2 Force](https://wiki.postmarketos.org/wiki/Motorola Moto Z2 Force (motorola-nash))
* [Motorola Moto G7 Power](https://wiki.postmarketos.org/wiki/Motorola Moto G7 Power (motorola-ocean))
* [Motorola Moto X4](https://wiki.postmarketos.org/wiki/Motorola Moto X4 (payton))
* [motorola Moto E4](https://wiki.postmarketos.org/wiki/Motorola Moto E4 (motorola-perry))
* [OnePlus 6](https://wiki.postmarketos.org/wiki/OnePlus 6 (oneplus-enchilada))
* [OnePlus 6T](https://wiki.postmarketos.org/wiki/OnePlus 6 (oneplus-enchilada))
* [OPPO Mirror 5s](https://wiki.postmarketos.org/wiki/Oppo Mirror5s (oppo-a51f))
* [Samsung Galaxy Ace 2](https://wiki.postmarketos.org/wiki/Samsung Galaxy Ace 2 (samsung-codina))
* [Samsung Nexus S](https://wiki.postmarketos.org/wiki/Samsung Nexus S (samsung-crespo))
* [Samsung Galaxy Grand Prime (CAN)](https://wiki.postmarketos.org/wiki/Samsung Galaxy Grand Prime CAN (samsung-gprimeltecan))
* [Samsung Galaxy Tab E 9.6 (SM-T561)](https://wiki.postmarketos.org/wiki/Samsung Galaxy Tab E 9.6 (SM-T561) (samsung-gtel3g))
* [Samsung Galaxy Tab E 9.6 (SM-T560)](https://wiki.postmarketos.org/wiki/Samsung Galaxy Tab E 9.6 (SM-T560) (samsung-gtelwifi))
* [Samsung Galaxy J5 2015](https://wiki.postmarketos.org/wiki/Samsung Galaxy J5 2015 (samsung-j5nlte))
* [Samsung Galaxy S III Neo](https://wiki.postmarketos.org/wiki/Samsung Galaxy S III Neo (samsung-s3ve3g))
* [Samsung Galaxy Xcover 2](https://wiki.postmarketos.org/wiki/Samsung Galaxy Xcover 2 (samsung-skomer))
* [Sony Xperia M2](https://wiki.postmarketos.org/wiki/Sony Xperia M2 (sony-eagle))
* [Sony Xperia M5](https://wiki.postmarketos.org/wiki/Sony Xperia M5 (sony-hollyss))
* [Sony Ericsson Xperia Mini Pro](https://wiki.postmarketos.org/wiki/Sony Ericsson Xperia Mini Pro (sony-mango))
* [Sony Xperia Z5](https://wiki.postmarketos.org/wiki/Sony Xperia Z5 (sony-sumire))
* [Sony Xperia XA](https://wiki.postmarketos.org/wiki/Sony Xperia XA (sony-tuba))
* [Vernee Thor](https://wiki.postmarketos.org/wiki/Vernee Thor (vernee-k506))
* [Xiaomi Mi 4i](https://wiki.postmarketos.org/wiki/Xiaomi Mi 4i (xiaomi-ferrari))
* [Xiaomi Mi 4c](https://wiki.postmarketos.org/wiki/Xiaomi Mi 4c (xiaomi-libra))
* [Xiaomi Mi Note 2](https://wiki.postmarketos.org/wiki/Xiaomi Mi Note 2 (xiaomi-scorpio))
* [Xiaomi Redmi Note 5 Plus](https://wiki.postmarketos.org/wiki/Xiaomi Redmi Note 5 Plus (xiaomi-vince))
[#grid end#]

<small>
*Thanks to: everyone who ported these devices, see the contributors section in each device's wiki page.*
</small>


## End of Part One

That was quite a lot of new exciting develpments in postmarketOS, but there's
more!  Part 2 will appear later this month. Once again, a huge *thank you* to
all of our contributors and great community for support. Stay tuned!

If you'd like to contribute, contact us, or participate in other ways, you can
find [information on joining our IRC/Matrix channels on the
wiki.](https://wiki.postmarketos.org/wiki/Matrix_and_IRC)
