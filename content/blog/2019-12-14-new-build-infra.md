title: "New postmarketOS build infrastructure is powered by sourcehut builds"
date: 2019-12-14
---
In January we've
[introduced](/blog/2019/01/16/600-days-of-postmarketOS/#new-srht-based-binary-repository)
the plan of building the whole binary repository of postmarketOS on
[sourcehut builds](https://sourcehut.org). This month we flicked the switch and
turned the system into production mode: we have successfully built all 1189 packages
(divide that by five architectures). It is rolled out as default mirror in
our swiss army knife of postmarketOS installation and development that is [pmbootstrap](https://gitlab.com/postmarketOS/pmbootstrap/).

[#grid side#]
[![](/static/img/2019-12/builds.sr.ht.jpg){: class="w300 border"}](https://builds.sr.ht/~postmarketos/job/121475)
[#grid text#]
In the first screenshot, you can see what a typical build job looks like. The
package that is building is noted on the left. Console output is neatly
divided into tasks, to make it easy to spot where a failure happened.
So far sourcehut builds works as it should, and it does not get in the way.
But if we should hit a bug that we can't reproduce elsewhere, we can [SSH into the failed
build](https://drewdevault.com/2019/08/19/Introducing-shell-access-for-builds.html)
and look around.
[#grid end#]

[#grid side#]
[![](/static/img/2019-12/bpo.jpg){: class="w300 border"}](https://build.postmarketos.org)
[#grid text#]

Development effort from our end went into
[build.postmarketos.org](https://build.postmarketos.org) (in short BPO). This is
the name of both the website seen in the second screenshot, as well as the
[source code](https://gitlab.com/postmarketOS/build.postmarketos.org/) for the
program that generates the website. Besides that, it manages the jobs that
run on sourcehut builds.

BPO has 91% test coverage. A rather unusual design decision is that the website
is generated as static HTML page whenever there is a change. It is not
generated on demand when requested via HTTP. This seems highly appropriate
though, as the content at most changes a few times per second.

We have come a long way from initially having no binary repository and
expecting all developers to build everything from source at the project's
public launch in May of 2017. During the following months we had an inofficial
repository of binary packages for Plasma Mobile packages on postmarketOS at one
point. Until we got the [first official binary
repository](/blog/2017/12/31/219-days-of-postmarketOS/#binary-repository) at
the end of 2017. But that one had to be manually triggered and the build logs
where not available online.

Now it's completely automated and transparent, and multiple developers of the
core team are able to fix things if they go south. Therefore we allow more
people to merge incoming patches, and it is already apparent that this has
resulted in increased productivity.
[#grid end#]

Last but not least, the new building infrastructure lays out the groundwork for
creating a new release channel of postmarketOS that will be based on the stable
release of Alpine. If you want to sneak a peek at how this will be done and
what else is planned for the new year, take a look at [the project direction
2020 meta
issue](https://gitlab.com/postmarketOS/postmarketos/issues/11).
