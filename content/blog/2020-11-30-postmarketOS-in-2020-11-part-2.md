title: "postmarketOS in 2020-11: Edge & Donations"
date: 2020-11-30
---
Here is the promised second part of the November 2020 update. The other half is
[here](/blog/2020/11/06/postmarketOS-in-2020-11-part-1/) if you missed it.

## News section for the 'edge' channel

Two weeks ago, a wlroots release was pushed to Alpine that caused Phosh to
crash. This is a good example of things that can go wrong when using the *edge*
channel of postmarketOS (as opposed to *stable*). The bug was
[reported](https://gitlab.com/postmarketOS/pmaports/-/issues/862) to the
postmarketOS issue tracker (precisely the right move!) and within the next
eight hours until we could close that issue, it was pinned down to the wlroots
0.12.0 upgrade, Phosh developers were informed, log messages were analyzed but
were not useful and eventually the "offending" commit was found with
`git bisect`. It turned out that the commit was a feature and not a bug, it
made wlroots terminate connections if some API protocol was not followed as
intended whereas it would just ignore this previously. An issue was created in
the [Phosh tracker](https://source.puri.sm/Librem5/phosh/-/issues/422), and a
patch was submitted to Alpine edge to revert that specific commit until Phosh
follows that specific API as it was intended (likely soon).

The story told above was certainly not worth writing a regular blog post about,
it was so quickly resolved that if each time we dealt with issues like these it
would be hard to find the proper blog posts among these edge breakage reports.
But still, it would be nice if there was something like a second blog where
people running postmarketOS edge can quickly find information about such issues
while they are ongoing. The solution we arrived at is a second blog, which will
only have such breakage reports from postmarketOS edge. Find it at
[postmarketos.org/edge](/edge).

## Donations

Time and again, we were asked if we accept donations. Today we are happy to
announce that all the paper work is done.
[Yes, we are ready for donations!](/donate.html)

Depending on where you live, the donation is tax deductible.
A variety of payment methods are available: from bank transfer to Bitcoin,
Bitcoin Cash, Namecoin, PayPal and credit card.
If you have an account set up
for any of these already, it should only take you a few minutes.

PINE64 used this mechanism to donate $10 for every sold PinePhone
postmarketOS community edition. Huge thanks to PINE64 and *to you* if you
bought one of them!

We will put the money into good use driving postmarketOS forward. To be
specific, [@MartijnBraam](https://gitlab.com/MartijnBraam) will be paid to work
on postmarketOS part time to do the tasks required to keep development up at a
good pace: reviewing merge requests, taking care of the infrastructure and
hacking cool new things into postmarketOS and upstream projects. This should
fill the void in 2021 when the
[NLnet grant](/blog/2020/05/31/three-years/#funding-from-nlnet) ends that is
currently enabling [@ollieparanoid](https://gitlab.com/ollieparanoid) to work
full time on postmarketOS.

From here on, the idea is to get enough (recurring) donations to make
postmarketOS sustainable for the future. To keep postmarketOS around. To keep
the OS in good shape that is made by like-minded people who demand
sustainability, maintainability, privacy and security to a level that none of
the mainstream OS are willing to deliver.

### Comments
* [Reddit](https://www.reddit.com/r/postmarketOS/duplicates/k47a39/postmarketos_in_202011_edge_donations/)
* [HN](https://news.ycombinator.com/item?id=25259987)
* [Mastodon](https://fosstodon.org/@postmarketOS/105301781092863078)
* [Twitter](https://twitter.com/postmarketOS/status/1333545783203913728)
