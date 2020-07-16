title: "PinePhone: postmarketOS community edition"
date: 2020-06-15
---

## Introduction

[#grid side#]
[![](/static/img/2020-06/pinephone-postmarketos-ce-back-thumb.png)](/static/img/2020-06/pinephone-postmarketos-ce-back.png)

[#grid text#]
We are proud to announce the PinePhone postmarketOS community edition!

postmarketOS was created to take a stand against the smartphone industry.
Compared to what we see on desktop machines, smartphones have artifically short
software update lifespans. You cannot even download updates for installed apps
without logging in. And unless you are extremely careful, the downloaded (or
even pre-installed) apps will turn the little device in your pocket into an
[advertising](https://developer.android.com/training/articles/ad-id)- and
[malware](https://arstechnica.com/information-technology/2020/03/found-malicious-google-play-apps-with-1-7-million-downloads-many-by-children/)-riddled
combination of
[big](https://www.forbes.com/sites/thomasbrewster/2020/04/30/exclusive-warning-over-chinese-mobile-giant-xiaomi-recording-millions-of-peoples-private-web-and-phone-use/)
[brother](https://www.techrepublic.com/article/facebook-data-privacy-scandal-a-cheat-sheet/)
and a [slot machine](https://medium.com/thrive-global/how-technology-hijacks-peoples-minds-from-a-magician-and-google-s-design-ethicist-56d62ef5edf3).

PINE64 breaks tradition with that very industry. Their PinePhone is not just
another Android based smartphone that inherits all of Android's problems.
Instead, PINE64 has focused on creating amazing hardware and encouraged many
alternative FLOSS smartphone OS developers to port their project to the
PinePhone.
[#grid end#]

## Linux enthusiasts only

Before we get into the details: postmarketOS is in beta state. The parts to
have basic smartphone functionallity with phone calls, SMS, mobile data, Wi-Fi,
and a touch friendly UI are there
([overview](https://gitlab.com/groups/postmarketOS/-/milestones/1)). But as of
writing, there are too many bugs to provide a reasonable user experience. We
will fix as much as we can over the next weeks, until the device is shipped
to everyone who has pre-ordered. More fixes and improvements will become
available over time through software updates. It should be possible to avoid
most future regressions with the new
[stable release channel](/blog/2020/05/31/three-years/#stable-release-channel).
Please have realistic expectations.

## The PinePhone

[#grid side#]

<div class="border" style="
	width: 350px;
	text-align: center;
	margin: 0px auto 30px auto;
">
<table class="table-specs">
<tr>
	<td>SoC</td>
	<td>Allwinner A64 Quad Core, Mali 400 MP2 GPU</td>
</tr><tr>
	<td>RAM</td>
	<td>2 GB, LPDDR3</td>
</tr><tr>
	<td>Display</td>
	<td>5.95″ LCD 720x1440, 18:9 (hardened glass)</td>
</tr><tr>
	<td>Internal storage</td>
	<td>16 GB eMMC</td>
</tr><tr>
	<td>Modem</td>
	<td>Quectel EG-25G with worldwide bands</td>
</tr><tr>
	<td>USB port</td>
	<td>Type C (power, data and HD digital video out)</td>
</tr><tr>
	<td>Wi-Fi</td>
	<td>802.11 b/g/n, single-band, hotspot capable</td>
</tr><tr>
	<td>Bluetooth</td>
	<td>4.0, A2DP</td>
</tr><tr>
	<td>GNSS</td>
	<td>GPS, GPS-A, GLONASS</td>
</tr><tr>
	<td>Rear Camera</td>
	<td>Single OV5640, 5 MP, 1/4″, LED flash</td>
</tr><tr>
	<td>Front Camera</td>
	<td>Single GC2145, 2 MP, f/2.8, 1/5″</td>
</tr><tr>
	<td>Sensors</td>
	<td>Accelerator, gyro, proximity, compass, barometer, ambient
	    light</td>
</tr><tr>
	<td>Buttons</td>
	<td>Up, down and power</td>
</tr><tr>
	<td>Killswitches</td>
	<td>LTE/GNSS, Wi-Fi/Bluetooth, microphone, speaker, cameras</td>
</tr><tr>
	<td>Battery</td>
	<td>Samsung J7 form-factor 3000 mAh</td>
</tr><tr>
	<td>Misc</td>
	<td>Headphone jack, micro SD slot, vibrator,<br>
	    pogo pin expansion header, RGB status LED</td>
</tr><tr>
</table>

Detailed specifications
</div>

[#grid text#]
Now let's talk about what gets us so excited about the PinePhone, besides their
community driven software approach. A quick rundown:


* [Mainline Linux kernel](https://gitlab.com/pine64-org/linux/) (with few
  patches and intention to upstream everything)
* [Free software GPU driver](https://gitlab.freedesktop.org/lima/web)
* Modem separated from main CPU
* Removable battery
* Bootable micro SD slot
* Headphone jack, that doubles as
  [serial port](https://wiki.pine64.org/PinePhone#Serial_console)
* Hardware killswitches

These features are crucial for privacy and security, and to give the device a
very long lifetime. We don't need to put an enormous amount of effort into
replacing an Android downstream kernel with a mainline Linux one, we have it
from the start. This is how smartphones should be made.
[#grid end#]

## postmarketOS community edition

Our community edition will be shipped with Phosh. We have considered shipping
with Plasma Mobile as well, and letting the user decide on the first boot. But
then we would have twice the effort to optimize the out-of-the-box experience.
If you don't like our decision, you can flash a Plasma Mobile postmarketOS (or
whatever UI and OS combination you like) image onto your PinePhone postmarketOS
CE at any time.

### User Interface: Phosh

Phosh is a <i>pho</i>ne <i>sh</i>ell running on top of various GNOME
components. It is developed by Purism for their own Linux smartphone, the
[Librem 5](https://puri.sm/products/librem-5/)
([comparison](https://tuxphones.com/yet-another-librem-5-and-pinephone-linux-smartphone-comparison/)),
which we have [promoted](/blog/2017/09/24/librem-5/) during their crowdfunding
campaign. If you like the looks of the modern GNOME desktop, you will feel
right at home with Phosh. See the screenshots below, and take a look at this
beautiful mockup of the
[calls](https://gitlab.gnome.org/Teams/Design/app-mockups/raw/master/calls/calls.png)
app to get a sense of the consistent design.

<div style="text-align: center">
<a href="/static/img/2020-06/phosh-lockscreen.png"><img
	src="/static/img/2020-06/phosh-lockscreen-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-06/phosh-homescreen.png"><img
	src="/static/img/2020-06/phosh-homescreen-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-06/phosh-pulldown.png"><img
	src="/static/img/2020-06/phosh-pulldown-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-06/phosh-menu.png"><img
	src="/static/img/2020-06/phosh-menu-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-06/phosh-browser.png"><img
	src="/static/img/2020-06/phosh-browser-thumb.jpg" class="w150 border"></a>
<a href="/static/img/2020-06/phosh-dialpad.png"><img
	src="/static/img/2020-06/phosh-dialpad-thumb.jpg" class="w150 border"></a>
</div>

### Full Disk Encryption

The PinePhone postmarketOS CE comes with our brand new
[on-device installer](https://wiki.postmarketos.org/wiki/On-device_installer).
It will ask you for a password on first boot, which it will use to set up an
encrypted installation. Full disk encryption has always been a priority of
postmarketOS, and with this new installation method, it can finally be used
without creating a custom image on the command-line. To our knowledge,
postmarketOS is the only non-Android free software phone operating system that
offers full disk encryption. But we hope that more of our friends' projects
adopt this in the future.


## Shut up, and take my money!

Pre-orders open early July 2020, see the
[PINE64 announcement](https://www.pine64.org/2020/06/15/june-update-postmarketos-ce-pinephone-shipping-pine64-cluster/).

Then you will be able to **[buy the postmarketOS PinePhone community edition
for $150](https://store.pine64.org/)**, plus shipping and handling costs (and
possibly import charges depending on your region). The PINE Store will donate
$10 to postmarketOS for each one that gets sold.

<i>Thanks to PINE64 and Purism for pushing the free software smartphone
revolution. Thanks to everybody who has contributed to postmarketOS, and in
context of this post, especially to the people who have contributed to make the
PINE64 devices and/or Phosh run with postmarketOS:
[@afontain](https://gitlab.com/afontain),
[@bshah](https://gitlab.com/bshah),
[@Cogitri](https://gitlab.com/Cogitri),
[@Danct12](https://gitlab.com/Danct12),
[@drebrez](https://gitlab.com/drebrez),
[@Icenowy](https://gitlab.com/Icenowy),
[@MartijnBraam](https://gitlab.com/MartijnBraam),
[@MayeulC](https://gitlab.com/MayeulC),
[@megi](https://xnux.eu/devices/pine64-pinephone.html),
[@Minecrell](https://gitlab.com/Minecrell),
[@ollieparanoid](https://gitlab.com/ollieparanoid),
[@PureTryOut](https://gitlab.com/PureTryOut),
[@z3ntu](https://gitlab.com/z3ntu)
</i>

## Comments

* [Reddit](https://www.reddit.com/r/postmarketOS/duplicates/h9iqiz/pinephone_postmarketos_community_edition/)
* [HN](https://news.ycombinator.com/item?id=23528571)
