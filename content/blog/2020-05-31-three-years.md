title: "Three years of postmarketOS"
date: 2020-05-31
---

Our blog posts became shorter and shorter, as we decided that currently time is
better spent on actual development than working two weeks on another epic blog
post. This three years update post follows suit, so take a big breath and
let us rush you through a few representative picks of what has been going on
in the depths of our git logs.

### Stable release channel

postmarketOS was always based on the bleeding edge version of <a
href="https://alpinelinux.org/">Alpine Linux</a>.
Since last week it's also possible to install postmarketOS based on the new
<a href="https://alpinelinux.org/posts/Alpine-3.12.0-released.html">3.12
stable</a> release of Alpine, in combination with a new stable v20.05 branch of
the postmarketOS packages (instead of master). This marks the first beta
release v20.05 of postmarketOS. It's a very rough one, polishing will be done
in the second beta. Most importantly, the stable release channel lets us avoid
breaking changes from upstream, and our infrastructure is ready for future
releases. Having a stable release channel has been a goal for years, and we
have finally completed it!

### Device categorization

We have over 200 booting devices now. Yes, *booting* is the operative word,
with most of these ports you get more of a Raspberry Pi alternative than a
functional phone experience with postmarketOS. Therefore, we started to
[categorize the devices](https://wiki.postmarketos.org/wiki/Devices). All
existing device ports have been moved to the *testing* category, and can be
moved to *community* or *main* depending on which features are working and how
well maintained a port is. Only *community* and *main* devices will be
cherry-picked to the stable branch.

Currently the only device in the *main* category is the QEMU virtual device.
It doesn't have any special hardware like a modem or GPS, so it was easy to
make it comply with the
[requirements for *main*](https://wiki.postmarketos.org/wiki/Device_categorization).
Once some minor changes are done to the PinePhone port, it can be moved from
*community* to *main* as well.

There are also some devices pending to be moved into *community* from *testing*,
like the Nokia N900, Xiaomi Redmi 4X, Motorola Moto G4 Play, Samsung Galaxy A3,
Samsung Galaxy A5, Samsung Galaxy S4 Mini Value Edition and Wileyfox Swift.
This is mostly possible, because they run a mainline Linux kernel already, or
in case of the MSM8916, are currently being mainlined. The MSM8974 devices are
also candidates, such as the Nexus 5, Fairphone 2, OnePlus One and the
Samsung Galaxy S5.

Earlier concepts of a channel-agnostic pmdevices repository were scrapped. This
would allow using the same device packages with both the edge and stable
channels, but at the price of making the device packages more complicated.
Instead of doing that, we will treat the device specific packages like other
packages and cherry-pick only the rather risk-free patches to the stable
branch.

### Mainline progress
[#grid side#]
[![](/static/img/2020-05/sm-a500f-thumb.png){: class="w200" }](/static/img/2020-05/sm-a500f.jpg)
[#grid text#]
If you are interested in mainlining your device, check out the all-new
[Mainlining](https://wiki.postmarketos.org/wiki/Mainlining) wiki page. It gives
an overview of all ongoing efforts, across 12 SoCs. For those, someone in the
[postmarketOS mainline](https://wiki.postmarketos.org/wiki/Matrix_and_IRC)
room should be able to get you started and help out to some extend. We have a
new [~postmarketos/upstreaming](https://lists.sr.ht/~postmarketos/upstreaming)
mailing list, which we put in CC for the patches we upstream into the Linux
kernel.

While we won't go into detail like
[last year](/blog/2019/06/23/two-years/#mainlining) and recount all the amazing
things that went on in the postmarketOS mainlining world since then, we can
point out one highlight:
[phone calls working on MSM8916 with audio!](https://gitlab.com/postmarketOS/pmaports/-/merge_requests/1233)

The photo shows a
[Samsung Galaxy A5 2015](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_A5_2015_(samsung-a5ulte))
running Plasma Mobile on a close to mainline kernel, one of the many new
mainline device ports that we have added to pmaports over the last year.
[#grid end#]

### Funding from NLnet

[@ollieparanoid](https://gitlab.com/ollieparanoid) will be able to work full
time on postmarketOS for the rest of the year. This is made possible by
[NLnet through the NGI0 PET Fund](https://nlnet.nl/project/postmarketOS/index.html).
Special thanks to his employer [sysmocom](https://www.sysmocom.de/) for being a
huge help in making this a reality.

### Raw numbers

Current stats and in brackets the diff to
[last year](/blog/2019/06/23/two-years/#raw-numbers):

- 607 people in the [main channel](https://wiki.postmarketos.org/wiki/Matrix_and_IRC) *(+364)*
- 5887 [/r/postmarketOS](https://www.reddit.com/r/postmarketOS/) readers *(+2821)*
- 2308 [merged MRs](https://gitlab.com/groups/postmarketOS/-/merge_requests?scope=all&utf8=%E2%9C%93&state=merged) *(+834)*
- 1422 [closed issues](https://gitlab.com/groups/postmarketOS/-/issues?scope=all&utf8=%E2%9C%93&state=closed) *(+435)*
- 458 [open issues](https://gitlab.com/groups/postmarketOS/-/issues?scope=all&utf8=%E2%9C%93&state=opened) *(+99)*
- 259 contributors in [pmaports.git](https://gitlab.com/postmarketOS/pmaports) (`git shortlog --summary --numbered | wc -l`) *(+86)*

### EOF

Join us in the effort to create a free software mobile operating system where
you truly own your phone, with updates until it physically falls apart! We have
a lot of tasks where you can help out, from hacking to blogging, it's all on
our [contributing](https://wiki.postmarketos.org/wiki/Contributing) page. For
new device porters specifically, check out our brand new
[#postmarketos-porting](https://wiki.postmarketos.org/wiki/Matrix_and_IRC)
channel.

To everyone who put their time and effort into postmarketOS, by now far too
many people to list here: you know who you are, thank you for making
postmarketOS possible. Together we can bring postmarketOS to the daily driver
goal!

### Comments

* [HN](https://news.ycombinator.com/item?id=23371793)
* [Reddit](https://old.reddit.com/r/postmarketOS/duplicates/gu4wc1/three_years_of_postmarketos/)
