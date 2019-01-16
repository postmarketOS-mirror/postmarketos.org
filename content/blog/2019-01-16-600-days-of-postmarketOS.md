title: "600 days of postmarketOS"
date: 2019-01-16
---

## Where Have You Been?

[#grid side#]
[![](/static/img/2019-01/Nexus5-wikipedia-thumb.jpg){: class="w300 border" }](/static/img/2019-01/Nexus5-wikipedia.jpg)

[#grid text#]
postmarketOS is aiming for a ten year life-cycle for smartphones, see the [all new front page](/) for a short introduction if you are new around here. Today we'll cover what happened during the second half of 2018. Many have been wondering where we've been and why it took us so long to write a real update post. Is the project dead already? Weren't phone calls almost working? What happened?
[#grid end#]

Development has been going on continuously, so we are not dead. Maybe a little undead though, like some of the old and forgotten phones we are trying to revive, because we have not really gotten any closer to the goal of getting telephony working or turning a phone into a daily driver. The Nexus 5, [while booting mainline with accelerated graphics and connecting to the cellular modem all with a free software userspace](/blog/2018/06/09/one-year/#nexus-5-floss-modem-stack-with-mainline), still does not have working audio. That is one example, other devices have different problems. However, we have not been sitting idle and doing nothing these past few months!

## What's Missing?
So you might think, "well, then suck it up and get that last missing piece about making calls in place, and there we have our daily driver and salvation from the Android/iOS duopoly" right? No, not at all. You see, even with that missing functionality, it's still a proof of concept and not something that can be easily used as a daily driver. Making a phone call on the Nexus 5 still requires firing up a terminal and inputting commands, to name the most obvious flaw.

But there is more. Like all Linux distributions, we need to take care of all the things below the surface. The list of housekeeping tasks include: integrating the various components with one another, updating software in the repositories and dealing with breakage from such updates, maintaining a binary package repository and repairing packages that fail to build, handling incoming patches, bug reports and feature requests, and writing and organizing documentation. These things slow development down, especially if they are not as optimized as they could be.

## What Now?
We are stuck in a proof-of-concept stage, and it's time to get out. No, this does not mean we are going to rush out telephony functionality (even if it could be done that "easily"), and pretending everything around it can be fixed later. There are certain workflows that need to be put in place to get a rock solid base, upon which it is easy and fun to develop on. Becoming a great platform for development has been the idea from the beginning, but it was only applied to the very foundation of postmarketOS: our [pmbootstrap](https://gitlab.com/postmarketOS/pmbootstrap) development tool. It's time to take it to the next level, and deploy this concept to the distribution as a whole.

## Aports Split From pmbootstrap.git
With that in mind, we took on one of the most long-standing issues we have had with the postmarketOS architecture: the package building recipes [(aports) were not separated from the pmbootstrap tool](https://gitlab.com/postmarketOS/pmbootstrap/issues/383). This is resolved now, pmbootstrap will clone its own copy of the now-separated [pmaports.git](https://gitlab.com/postmarketOS/pmaports) repository as you run its initialization wizard the first time. Thanks to this new independence, Linux distributions can properly package pmbootstrap. This change has also allowed us to (finally!) put it up on [pypi](https://pypi.org/project/pmbootstrap):

```shell-session
$ pip install --user pmbootstrap
$ pmbootstrap init
```

This was also a very important stepping stone for basing our packages [on different Alpine Linux branches in the future](https://gitlab.com/postmarketOS/pmaports/issues/5). Right now, we are on Alpine's bleeding edge (aptly named "edge") branch. While this allows us to get the latest versions of packages quickly it is a moving target, and roughly once a month there is an update in one of the packages that causes [substantial breakage](https://gitlab.com/postmarketOS/pmaports/issues/144) throughout postmarketOS. As developers, this is not a fun situation, but we can deal with it. Typically after a few days, everything is adjusted on our end, but we don't need to tell you how unacceptable it would be if your phone refused to work for a few days. Especially when every so often the "fix" involves having to reinstall the OS. Therefore the plan is to use Alpine stable releases in the future as a base, and rebasing our packages in a separate branch on the next Alpine release roughly every six months (to match Alpine's release cycle). This will allow us to give users a clear and safe upgrade path from the current stable packages branch to the new one once it is ready.

## New sr.ht Based Binary Repository
Having multiple package branches means that we need to build each package for each branch, for every CPU architecture. Of course, this is not a fun exercise without a powerful and automated package building infrastructure. The problem is, what we have right now is not cut out for that task: a single x86_64 machine with a 3 GHz Quad-Core that is manually triggered to build everything. It takes, for example, several hours to build new Plasma Mobile upgrades for all supported architectures even though we are cross compiling and not supporting multiple branches yet.

This prompted us to start brainstorming for a [worthy successor](https://gitlab.com/postmarketOS/postmarketos.org/issues/78). Not long after the discussion started, [builds.sr.ht](https://builds.sr.ht) ("builds dot sir hat") was mentioned and we have since started collaborating with its author [@SirCmpwn](https://gitlab.com/SirCmpwn). He [describes](https://drewdevault.com/2018/11/15/sr.ht-general-availability.html)
his project as:

> *The flagship product from sr.ht is its continuous integration platform, builds.sr.ht, which is easily the most capable continuous integration system available today. It’s so powerful that I’ve been working with multiple Linux distributions on bringing them onboard because it’s the only platform which can scale to the automation needs of an entire Linux distribution. [...]*

[@MartijnBraam](https://gitlab.com/MartijnBraam) [has been working on backend code](https://gitlab.com/postmarketOS/build.postmarketos.org/issues/3) that will start the individual package build jobs whenever new commits land in pmaports.git. It comes with a nice status page frontend, which links the individual postmarketOS packages to their sr.ht build jobs. Having one job per package requires knowledge of which packages need to be built in advance, so [@ollieparanoid](https://gitlab.com/ollieparanoid) added [`pmbootstrap repo_missing`](https://gitlab.com/postmarketOS/pmbootstrap/merge_requests/1717).

The sr.ht based build repository efforts are still work in progress, however we have already caused nice spikes in sr.ht's statistics as we triggered the initial package build (*see image below*).

[![](/static/img/2019-01/srht_building_pmos_packages.png){: class="wfull border" }](/static/img/2019-01/srht_building_pmos_packages.png)


## Improved Nexus 5 Mainline Packaging

[#grid side#]
[![](/static/img/2019-01/nexus5-surfing-thumb.jpg){: class="w200 border"}](/static/img/2019-01/nexus5-surfing.png)

[#grid text#]
[@pparent](https://gitlab.com/pparent) figured out why the Nexus 5 was not booting reliably and [fixed it](https://gitlab.com/postmarketOS/pmaports/merge_requests/44). Furthermore he made sure that [all backlights of the phone are used](https://gitlab.com/postmarketOS/pmaports/merge_requests/33), instead of only having half of them activated.

In the picture you can see that he [enabled the Plasma style](https://gitlab.com/postmarketOS/pmaports/commit/87e3d17721d9fcb6f188b15e004ca9637d156132) for the QtVirtualKeyboard, and was able to do some basic web browsing with the device. Check out [this video](https://www.youtube.com/watch?v=6DqB4PVfREU) where he uses his [mobile-configured QtWebBrowser](https://gitlab.com/postmarketOS/pmaports/merge_requests/16) on top of Plasma Mobile to visit various websites, watches a video in the browser and uses touch gestures with OpenStreetMap.
[#grid end#]

## Pine A64-LTS, Librem 5, NC_1

While the majority of the devices running postmarketOS are rather old ones, we are interested in packaging support for new hardware as well. Especially if that hardware is produced by free software loving companies such as [PINE64](https://www.pine64.org/), [Purism](https://puri.sm/) and [Necuno Solutions](https://necunos.com/).

[#grid side#]
[![](/static/img/2019-01/Pine-a64lts-playbox-thumb.jpg){: class="w300 border"}](/static/img/2019-01/Pine-a64lts-playbox.jpg)
[#grid text#]
Let's go through the related news in chronological order. After the PINE64 CEO TL Lim saw our [postmarketOS presentation at Akademy](/blog/2018/08/25/postmarketos-at-akademy/), he offered us free Pine A64-LTS devices and shipped them shortly afterwards. [@MartijnBraam](https://gitlab.com/MartijnBraam) [did the port](https://gitlab.com/postmarketOS/pmaports/merge_requests/6) with a lot of help from [@z3ntu](https://gitlab.com/z3ntu) and extended pmbootstrap to be able to [write the U-Boot bootloader to the SD card](https://gitlab.com/postmarketOS/pmbootstrap/merge_requests/1693).
[#grid end#]
[#grid side#]
[![](/static/img/2019-01/Librem5-devkit-thumb.jpg){: class="w300 border"}](/static/img/2019-01/Librem5-devkit.jpg)
[#grid text#]
Next up is Purism's Librem 5. [@craftyguy](https://gitlab.com/craftyguy) ordered the development kit back in the [crowdfunding days](/blog/2017/09/24/librem-5) in September 2017. It arrived a few weeks ago and, while we were writing this blog post, he [managed to boot postmarketOS on it](https://gitlab.com/postmarketOS/pmaports/merge_requests/141). Sharing as much code between all devices as possible has paid off once more, because the Librem 5 requires U-Boot to be written to the SD card too. It also needs another firmware file to be written there, so [@craftyguy](https://gitlab.com/craftyguy) [refactored](https://gitlab.com/postmarketOS/pmbootstrap/merge_requests/1739) the code to allow an arbitrary number of firmware files to be embedded into the SD card images. In the picture you can see the dev board booted into XFCE4 and hooked up to a HDMI monitor.
[#grid end#]

Last but not least is [Necuno Solutions with their NC_1](https://necunos.com/news/necunos-nc_1-and_ne_1-press-release/). They are collaborating with six alternative mobile OS communities, and [postmarketOS is among them](https://necunos.com/blog/necuno-solutions-and-postmarketos-collaboration/). [@PureTryOut](https://gitlab.com/PureTryOut) will receive one device for free for porting purposes, and it is possible to order the NC_1 with postmarketOS pre-installed. Which of course brings back some classic questions: *When a device is sold with postmarketOS, should we just name it marketOS then? What about premarketOS or pre-postmarketOS?* (More work is clearly needed here.)

## Raspberry Pi Zero

[#grid side#]
[![](/static/img/2019-01/RaspberryPiZeroWeston-thumb.jpg){: class="w300 border" }](/static/img/2019-01/RaspberryPiZeroWeston.jpg)

[#grid text#]
As shown in the last big update post, we have [support for all Raspberry Pi](/blog/2018/06/09/one-year/#raspberry-pi-samsung-galaxy-tab-101-and-nokia-n9) versions up to 3B+ in postmarketOS. This already included the Raspberry Pi Zero, but since we had the DHCP server disabled for all Pi models, there was no convenient way to boot the Zero: it does not come with an ethernet port like the other models.

[@drebrez](https://gitlab.com/drebrez) took care of it by making [several related fixes](https://gitlab.com/postmarketOS/pmaports/issues/151) and introducing a [separate device package](https://gitlab.com/postmarketOS/pmaports/merge_requests/125), along with [updated wiki documentation](https://wiki.postmarketos.org/wiki/Raspberry_Pi) to provide installation instructions for each model.
[#grid end#]

## Unity 8 and Phosh

[#grid side#]
[![](/static/img/2019-01/unity8.png){: class="w300"}](/static/img/2019-01/unity8.png)

[#grid text#]
You may remember Canonical's canceled attempt to bringing Ubuntu's Unity desktop to the phone. It was called Ubuntu Touch and lives on without Canonical's backing in the form of [ubports](https://ubports.com/), who have forked the project and maintain it nowadays. [@z3ntu](https://gitlab.com/z3ntu) started [porting the interface to postmarketOS](https://gitlab.com/postmarketOS/pmaports/merge_requests/27) and has already done an impressive amount of upstreaming with everything he fixed along the way. Unity 8 boots up so far, ubuntu-app-launch is working enough that applications can launch but everything locks up easily at this point. We need to package some actual apps as well, right now there is only the system settings app (*in the picture*).
[#grid end#]

Meanwhile, [@PureTryOut](https://gitlab.com/PureTryOut), [@ollieparanoid](https://gitlab.com/ollieparanoid) and [@MartijnBraam](https://gitlab.com/MartijnBraam) took a shot at [packaging Phosh](https://gitlab.com/postmarketOS/pmaports/merge_requests/8), the UI that the Librem 5 will use by default on Purism's PureOS. Just like the Unity 8 port, getting the UI running on Alpine's stack holds some unresolved challenges and help is highly appreciated.


## Misc Changes
As always with these blog posts, they get long even if we don't bother listing each and every change. Here are some of the most noteworthy ones.

[Tab completion for pmbootstrap](https://wiki.postmarketos.org/wiki/Installing_pmbootstrap) works *perfectly* now for bash and zsh: [@GrantM11235](https://gitlab.com/GrantM11235) added this support by [using argcomplete](https://gitlab.com/postmarketOS/pmbootstrap/merge_requests/1656), so it automatically does the tab completions from the existing argparse. It does this without manual maintenance, and always perfect! Isn't that nice?

Until recently we had to use ARMv6 binaries on the devices with ARMv7 CPUs, because ARMv7 was not available in Alpine and postmarketOS. This [is no longer the case](https://gitlab.com/postmarketOS/pmbootstrap/issues/238)! We should be able to unleash the full CPU power shortly for all devices, as [@PureTryOut](https://gitlab.com/PureTryOut) tested that [changing the architecture for the Sony Xperia Z1 Compact](https://gitlab.com/postmarketOS/pmaports/merge_requests/126) works flawlessly.

One of the tougher challenges for postmarketOS was Alpine's [upgrade from GCC-6 to GCC-8](https://gitlab.com/postmarketOS/pmaports/issues/144). A lot of vendor kernels refused to compile with GCC-8, and at least one device doesn't boot with a kernel compiled by GCC-8. We ended up with packaging GCC-6 side-by-side with GCC-8, building all existing kernels with GCC-6 and allowing device owners the ability to select the GCC version that should be used in each [vendor kernel package](https://wiki.postmarketos.org/wiki/Vendor_kernel_specific_package). Device owners have been slowly switching to GCC-8 since then, after carefully testing that their device still boots after the change. New default patches related to GCC-8 were added, so new ports don't have to deal with these issues.

[@pinoaffe](https://gitlab.com/pinoaffe) updated the initramfs script to look for the rootfs in [all block devices and partitions](https://gitlab.com/postmarketOS/pmaports/merge_requests/61). Speaking of the rootfs, [@zhuowei](https://gitlab.com/zhuowei) made it possible to [build rootfs images with non-512 byte sector sizes](https://gitlab.com/postmarketOS/pmbootstrap/merge_requests/1725) (required for the Google Pixel 3 XL).

Two other important project changes, which aren't necessarily related to each other, are that [@ryang2678](https://gitlab.com/ryang2678) [packaged the grate driver](https://gitlab.com/postmarketOS/pmaports/merge_requests/67) (for Tegra GPUs), and the wiki main page and [homepage](https://gitlab.com/postmarketOS/postmarketos.org/merge_requests/71) (based on [@pparent](https://gitlab.com/pparent)'s excellent photos) have been updated to be more mobile friendly by [@ollieparanoid](https://gitlab.com/ollieparanoid).

## Eating Our Own Dog Food

[#grid side#]
[![](/static/img/2019-01/N900-i3wm-mpd-thumb.jpg){: class="w300 border" }](/static/img/2019-01/N900-i3wm-mpd.jpg)

[#grid text#]
A great way to increase stability is [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food):
using postmarketOS installations on our own devices every other day for certain tasks. One example is turning the Nokia N900 into a music player with i3wm and mpd. This effort has already spawned [a few usability improvement patches](https://gitlab.com/postmarketOS/pmaports/merge_requests/72) and [lots of resulting ideas](https://wiki.postmarketos.org/wiki/User:Ollieparanoid/Dogfooding:N900). It turns out this idea was not exactly unique as at least [one other person has created a very similar setup for their N900](https://twitter.com/betojsp/status/1060336080287883264). If you would like to join us on the dogfooding journey, figure out your own use case (e.g. how about a podcast player, or a browser that displays a status page? Tracking habits or TODOs?).
[#grid end#]

Then document your progress [in the wiki](https://wiki.postmarketos.org/wiki/Category:Dogfooding) and reach out to the [Community](https://wiki.postmarketos.org/wiki/Category:Community) to share your results, work together on fixing the flaws you found, and optimizing postmarketOS for your use case.

## 28 new booting devices (112 total)

[#grid side#]
<!-- <br>s added to force each image to be in their own line, even around 790px screen width -->
[![](/static/img/2019-01/Semc-smultron-thumb.png){: class="w300" }](/static/img/2019-01/Semc-smultron.png) <br>
[![](/static/img/2019-01/Ouya-thumb.jpg){: class="w300 border" }](/static/img/2019-01/Ouya.jpg) <br>
[![](/static/img/2019-01/Huawei-Cameron-thumb.jpg){: class="w300 border" }](/static/img/2019-01/Huawei-Cameron.jpg)

[#grid text#]
<!-- Generated with: 'pmos-stats new-devices 39d62928cbeefa9f0aa8a1625d75df3d6ceee8dd --md'
     Current master (for next time): a6560dc6caa66361a8c3de2c0e652867bc51f8c3
     Device count taken from what 'pmbootstrap init' says -->

* [Asus MeMO Pad FHD 10 (ME302KL) `asus-duma`](https://wiki.postmarketos.org/wiki/ASUS_MeMO_Pad_FHD_10_(asus-duma))
* [Asus MeMo Pad 7 `asus-me176c`](https://wiki.postmarketos.org/wiki/Asus_MeMo_Pad_7(me176c(x)))
* [Asus Zenfone 2 Laser/Selfie (1080p) `asus-z00t`](https://wiki.postmarketos.org/wiki/Asus_Zenfone_2_Laser/Selfie_(1080p)_(asus-z00t))
* [Asus Zenfone Go `asus-z00vd`](https://wiki.postmarketos.org/wiki/ASUS_Zenfone_Go_(asus-z00vd))
* [BQ Aquaris U `bq-chaozu`](https://wiki.postmarketos.org/wiki/Aquaris-U)
* [Fairphone 1 `fairphone-fp1`](https://wiki.postmarketos.org/wiki/Fairphone_1_(fairphone-fp1))
* [Google Pixel 3 XL `google-crosshatch`](https://wiki.postmarketos.org/wiki/Google_Pixel_3_XL_(google-crosshatch))
* [Huawei Mediapad M5 Pro `huawei-cameron`](https://wiki.postmarketos.org/wiki/Huawei_Mediapad_M5_pro_(huawei-cameron)) *(third picture)*
* [LG L70 `lg-w5`](https://wiki.postmarketos.org/wiki/LG_L70_(lg-w5))
* [Motorola Moto X (2013) `motorola-ghost`](https://wiki.postmarketos.org/wiki/Moto_X)
* [Motorola Moto E (2nd Gen) `motorola-surnia`](https://wiki.postmarketos.org/wiki/Moto_E_(motorola-surnia))
* [Nokia Lumia 720 `nokia-rm885`](https://wiki.postmarketos.org/wiki/Nokia_Lumia_720)
* [Ouya `ouya-ouya`](https://wiki.postmarketos.org/wiki/Ouya_(ouya-ouya)) *(second picture)*
* [PINE A64-LTS `pine-a64lts`](https://wiki.postmarketos.org/wiki/Pine_A64-LTS_(pine-a64lts))
* [Raspberry Pi Zero `raspberry-pi0`](https://wiki.postmarketos.org/wiki/Raspberry_Pi_Zero)
* [Raspberry Pi 3 `raspberry-pi3`](https://wiki.postmarketos.org/wiki/Raspberry_Pi)
* [Samsung SIII mini Value Edition `samsung-i8200`](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_SIII_mini_Value_Edition_(samsung-i8200))
* [Samsung Galaxy Trend Plus `samsung-kylepro`](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_Trend_Plus_(samsung-s7580))
* [Samsung Trend Lite `samsung-kylevess`](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_Trend_lite_(s7390g))
* [Samsung Galaxy S4 Mini (dual sim) `samsung-serranodsdd`](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_S4_Mini_dual_sim)
* [Sony Ericsson Xperia mini `semc-smultron`](https://wiki.postmarketos.org/wiki/Sony_Ericsson_Xperia_mini_(semc-smultron)) *(first picture)*
* [Sony Live with Walkman `sony-coconut`](https://wiki.postmarketos.org/wiki/Sony_Ericsson_Live_With_Walkman_(sony-coconut))
* [Sony Xperia M `sony-nicki`](https://wiki.postmarketos.org/wiki/Sony_Xperia_M_(sony-nicki))
* [Sony Xperia L `sony-taoshan`](https://wiki.postmarketos.org/wiki/Sony_Xperia_L_(sony-taoshan))
* [Sony Xperia M4 Aqua `sony-tulip`](https://wiki.postmarketos.org/wiki/Sony_Xperia_M4_Aqua_(sony-tulip))
* [Various tablets with atom CPU `tablet-x64uefi`](https://wiki.postmarketos.org/wiki/Generic_x64_uefi)
* [Xiaomi Redmi 2 `wingtech-wt88047`](https://wiki.postmarketos.org/wiki/Xiaomi_Redmi_2_(wingtech-wt88047))
* [Xiaomi Mi 3 `xiaomi-cancro`](https://wiki.postmarketos.org/wiki/Xiaomi_Mi_3_(cancro))
[#grid end#]
*Thanks to: everyone who ported these devices, see the contributors section in each device's wiki page.*

## Raw Numbers

As in all the big update blog posts, here are some additional figures. Note that the merged MRs, closed issues, open issues are counted across [all postmarketOS related repositories](https://gitlab.com/postmarketOS) now (this was not possible on GitHub, but [we moved to GitLab](/blog/2018/06/27/moving-to-gitlab/)). Stars, forks and watches are not included, as these were not imported. See the [last post](/blog/2018/06/09/one-year/#raw-numbers) for reference.

- 415 people in the [channel](https://wiki.postmarketos.org/wiki/Matrix_and_IRC) (+65)
- 2092 [/r/postmarketOS](https://www.reddit.com/r/postmarketOS/) readers (+336)
- 1145 [merged MRs](https://gitlab.com/groups/postmarketOS/-/merge_requests?scope=all&utf8=%E2%9C%93&state=merged)
- 845 [closed issues](https://gitlab.com/groups/postmarketOS/-/issues?scope=all&utf8=%E2%9C%93&state=closed)
- 251 [open issues](https://gitlab.com/groups/postmarketOS/-/issues?scope=all&utf8=%E2%9C%93&state=opened)
- 133 contributors in [pmaports.git](https://gitlab.com/postmarketOS/pmaports) (`git shortlog --summary --numbered | wc -l`) *(+27)*

## Closing Words

[FOSDEM 2019](https://fosdem.org/2019/) starts in roughly two weeks, and quite a few people from postmarketOS will attend ([@bshah](https://gitlab.com/bshah), [@MartijnBraam](https://gitlab.com/MartijnBraam), [@MayeulC](https://gitlab.com/MayeulC), [@PureTryOut](https://gitlab.com/PureTryOut), [@unrznbl](https://gitlab.com/unrznbl) and [@z3ntu](https://gitlab.com/z3ntu)), together with folks from pretty much every alternative FLOSS mobile project out there. Looking forward to seeing you there, if you are going!

So this has been a mixed bag of news. But here we are, honest and still having fun celebrating the hacker spirit that flows through the project. Thanks for reading and good luck with whatever your passion is, let's make 2019 a marvelous year of overcoming our obstacles, having fun and hacking on fascinating stuff!

## Comments

* [Reddit](https://old.reddit.com/r/postmarketOS/duplicates/agj2u0/600_days_of_postmarketos/)
* [HN](https://news.ycombinator.com/item?id=18919101)
