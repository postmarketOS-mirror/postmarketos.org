title: "Four years of postmarketOS /\nAlpineConf 2021"
date: 2021-05-26
---

### Happy 4th birthday!
"Bend an existing Linux distribution to run on smartphones." This is what we
set out to do
[four years ago](/blog/2017/05/26/intro/#we-can-fix-this-as-a-community), and
it has been quite the success. Alpine Linux, with the thin postmarketOS layer
on top, is now able to _boot_ on an ever increasing, insane number of currently
289 [mobile devices](https://wiki.postmarketos.org/wiki/Devices).

[#grid side#]
[![](/static/img/2018-06/wallpaper-darkside-thumb.jpg){: class="w300 border"}](/static/img/2018-06/wallpaper-darkside.png)
[#grid text#]
While most of these run downstream Linux kernels and can only be used as
Raspberry Pi-like tinkering devices, it is still a huge accomplishment by our
amazing community. But even greater feats are the devices running
[(close to) mainline](https://wiki.postmarketos.org/wiki/(Close_to)_Mainline)
kernels, such as the eleven phones present in our
[latest release](/blog/2021/03/31/v21.03-release/). These became quite usable
for Linux enthusiasts, and some people are daily driving them.
[#grid end#]

There is still lots of work to do, but at the same time it is clear
now that the concept of running real Linux distributions on smartphones has a
foot in the door. As the PinePhone and Librem 5 showed up, more and more
amazing projects with similar missions were started on a wide range of Linux
distributions. This has lead to more people getting involved, and more
collaborations upstream. Most notably [Mobian](https://mobian-project.org), who
we have a long history of collaborating with on projects like osk-sdl, the
on-device installer, PinePhone modem improvements and other components. We
congratulate the Mobian developers for
[adding support for two mainlined SDM845 Android phones](https://blog.mobian-project.org/posts/2021/05/17/update-2021-05-17/).
Linux distributions on smartphones are here to stay!

### AlpineConf 2021

Back to our own distribution and what we are based on: the first AlpineConf
ever has taken place online on the 15th and 16th of May 2021.
[Lots of enjoyable talks](https://ariadne.space/2021/05/18/alpineconf-2021-recap/)
([videos](https://gitlab.alpinelinux.org/alpine/alpineconf-cfp/-/issues),
[Q&As](https://bbb.dereferenced.org/b/adm-ec4-bx7-ypm)) covered everything from
infrastructure to running Alpine on mainframes. Below are the presentations
(with Q&As appended) from the postmarketOS track.

#### pmbootstrap: the Swiss Army knife of postmarketOS development
[#grid side#]
[![](/static/img/2021-05/talk-pmbootstrap.jpg){: class="w300 border"}](https://diode.zone/videos/watch/3476503c-6ca1-4628-a8e6-0d893def81b9)
[#grid text#]
@ollieparanoid introduces pmbootstrap, demonstrates how to set it up and how to
do the most common tasks (install pmOS, build packages and host your own repo,
port a new device, run QEMU). There's also a pmaports.git tour and a brief
dive into advanced features.

[#grid end#]
62 min | video:
[diode.zone](https://diode.zone/videos/watch/3476503c-6ca1-4628-a8e6-0d893def81b9)
(PeerTube),
[odysee.com](https://odysee.com/@postmarketOS:1/alpineconf-2021-oliver:5)
(LBRY)
| [slides](/static/slides/2021-alpineconf-pmbootstrap/)

#### Showing off postmarketOS
[#grid side#]
[![](/static/img/2021-05/talk-showing-off.jpg){: class="w300 border"}](https://diode.zone/videos/watch/fa006d69-3934-4397-81ba-f696349868d3)
[#grid text#]
@MartijnBraam shows his incredibly large collection of phones, and how it looks
like when you put postmarketOS with various user interfaces on them. Besides
the popular three (Phosh, Plasma Mobile, Sxmo), lesser known UIs like Shelli
are also covered.

[#grid end#]
28 min | video:
[diode.zone](https://diode.zone/videos/watch/fa006d69-3934-4397-81ba-f696349868d3)
(PeerTube),
[odysee.com](https://odysee.com/@postmarketOS:1/alpineconf-2021-postmarketos-demo:e)
(LBRY)

#### Sxmo: Simple X Mobile - A minimalist environment for Linux smartphones
[#grid side#]
[![](/static/img/2021-05/talk-sxmo.jpg){: class="w300 border"}](https://diode.zone/videos/watch/b52e7c40-87cb-4479-a4cc-c11b1bfa8806)
[#grid text#]

@anjandev, @milesalan and @proycon explain the concept of running the tiling
window manager [dwm](https://dwm.suckless.org/) and other suckless tools on a
smartphone with [Sxmo](https://sr.ht/~mil/Sxmo/), and then prove
in this mind-blowing talk that it actually works. Quoting @anjandev from the
Q&A: "I cannot go back to an Android anymore."

[#grid end#]
29 min | video:
[diode.zone](https://diode.zone/videos/watch/b52e7c40-87cb-4479-a4cc-c11b1bfa8806)
(PeerTube),
[odysee.com](https://odysee.com/@postmarketOS:1/alpineconf-2021-oliver:5)
(LBRY)

### Comments
* [Mastodon](https://fosstodon.org/@postmarketOS/106302868167016914)
* [Lemmy](https://lemmy.ml/post/67466)
<small>
* [Hacker News](https://news.ycombinator.com/item?id=27294222)
* [Twitter](https://twitter.com/postmarketOS/status/1397619417211621378)
* [Reddit](https://www.reddit.com/r/linux/comments/nlo0j3/four_years_of_postmarketos_alpineconf_2021/)
([2](https://www.reddit.com/r/postmarketOS/comments/nlnzph/four_years_of_postmarketos_alpineconf_2021/))
</small>
