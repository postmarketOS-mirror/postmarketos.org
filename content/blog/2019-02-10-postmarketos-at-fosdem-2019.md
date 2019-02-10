title: "postmarketOS at FOSDEM 2019"
date: 2019-02-10
---

Last weekend was [FOSDEM 2019](https://fosdem.org/2019/), Europe's biggest event for open-source and free software developers to meet, share ideas and collaborate. A few postmarketOS developers and community members attended, as well as several other Linux phone project members. Of course, besides just walking around and attending several interesting talks, we also took this opportunity to do some work!

The PINE64 company was present with their own stand, and a PINE64 community meeting in the evening. They showed off their almost ready PinePhone development kits, and some other neat hardware like a fully open-source IP camera, their new Pinebook Pro and PineTablet. Since [@z3ntu](https://gitlab.com/z3ntu), [@MartijnBraam](https://gitlab.com/MartijnBraam) and [@PureTryOut](https://gitlab.com/PureTryOut) took their Pine A64-LTS kits with them (which uses basically the same hardware as will be in the PinePhone), we decided to do some work improving our port, and we got the screen working for the first time!

[![](/static/img/2019-02/fosdem-pmos-pine64.jpg){: class="wfull border"}](/static/img/2019-02/pmos-fosdem-pine64.jpg)

There is still work to do as the touchscreen doesn't respond yet, and the patches to make the display work still have to be combined with our current kernel sources. However, with the progress we're currently making, it means we should have a working port once the actual phone releases!

We've also met the people behind Necunos and their first mobile device, the NC_1. Originally the plan was for us to receive a devkit at FOSDEM, but due to an issue with the screen they had chosen originally, this is delayed till later this month. They did however have a prototype with them, and it was awesome to see it in person. We're waiting for the devkit in excitement, and hopefully next year they'll have a stand as well.

An event like FOSDEM is also a good opportunity to meet with related and collaborating projects. We've met [@MerlijnWajer](https://gitlab.com/MerlijnWajer) from [Maemo Leste](https://maemo-leste.github.io/), [@UniversalSuperBox](https://gitlab.com/UniversalSuperBox) from [UBPorts](https://ubports.com/), [@SirCmpwn](https://gitlab.com/SirCmpwn) from [sourcehut](https://sourcehut.org/) (which [will soon be building our packages](/blog/2019/01/16/600-days-of-postmarketOS/#new-srht-based-binary-repository) and automatically push them to our repo), and [@bshah](https://gitlab.com/bshah) from [Plasma Mobile](https://plasma-mobile.org).

[![](/static/img/2019-02/fosdem-community-thumb.jpg){: class="wfull border"}](/static/img/2019-02/fosdem-community.jpg)

From left to right:
[@bshah](https://gitlab.com/bshah),
[@MayeulC](https://gitlab.com/MayeulC),
[@unrznbl](https://gitlab.com/unrznbl),
[@z3ntu](https://gitlab.com/z3ntu),
[@MerlijnWajer](https://gitlab.com/MerlijnWajer),
[@UniversalSuperBox](https://gitlab.com/UniversalSuperBox),
[@PureTryOut](https://gitlab.com/PureTryOut),
[@NotKit](https://gitlab.com/NotKit),
[@MartijnBraam](https://gitlab.com/MartijnBraam)

The future of Linux on phones is definitely bright, which was just reconfirmed by the awesome people and companies we've met this year. We'll probably hold a talk ourselves next year, and hopefully we'll meet even more people. 🎉

## Comments

* [Reddit](https://old.reddit.com/r/postmarketOS/duplicates/ap6qob/postmarketos_at_fosdem_2019/)
* [Hacker News](https://news.ycombinator.com/item?id=19129192)
