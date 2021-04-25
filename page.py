# Copyright 2021 Oliver Smith
# SPDX-License-Identifier: GPL-3.0-or-later
import html

import config.download
import config.mirrors

def grid(html):
    """ Replace the following markers with appropriate <div class="..."> and
        </div> tags. See README.md and static/code/blog-post.css for more
        information.
        - "[#grid side#]"
        - "[#grid text#]"
        - "[#grid bottom#]"
        - "[#grid end#]"
        :param html: blog post code (already converted from markdown to HTML)
        :returns: html with all markers replaced """
    sections = ["side", "text", "bottom"]
    ret = ""
    in_grid = False

    for word in html.split("[#grid "):
        # Continue or start grid
        if in_grid:
            # Avoid "<p></div>"
            if ret[-3:] == "<p>":
                ret = ret[:-3]
            ret += "</div>"

        # New grid section
        tag_found = ''
        for section in sections:
            tag = section + "#]"
            if word.startswith(tag):
                tag_found = tag
                if not in_grid:
                    ret += '<div class="grid">'
                    in_grid = True
                ret += '<div class="grid-' + section + '">'
                break

        # End grid
        tag = "end#]"
        if word.startswith(tag):
            if not in_grid:
                raise ValueError("[#grid end#] found before it was opened!")
            tag_found = tag
            ret += "</div>"
            in_grid = False

        # Remove tag from word
        word = word[len(tag_found):]

        # Avoid "<div class=...></p>"
        if word[:4] == "</p>":
            word = word[4:]

        ret += word

    # Check for grids without end tag
    if in_grid:
        raise ValueError("Missing [#grid end#]!")
    return ret


def download_table(html):
    marker = "[#download table#]"
    if marker not in html:
        return html

    imgs_url = config.download.imgs_url
    latest_release = config.download.latest_release

    new = "<table class='table-specs'>\n"

    for category, category_cfg in config.download.table.items():
        new += f"<tr><td colspan='4'><b>{category}</b></td></tr>\n"
        for device, device_cfg in category_cfg.items():
            name = device_cfg["name"]
            link = f"{imgs_url}/{latest_release}/{device}/"
            new += "<tr><td style='padding: 0px 10px'>\n" \
                   f"\t<a href='{link}'>{name}</a>\n" \
                   "</td></tr>\n"

    new += "</table>\n"
    return html.replace(marker, new)


def mirrors_list(html_str):
    marker = "[#mirrors list#]"
    if marker not in html_str:
        return html_str

    new = ""
    for name, mirror_cfg in config.mirrors.mirrors.items():
        urls_html = ""
        for url in mirror_cfg["urls"]:
            protocol_esc = html.escape(url.split(":", 1)[0])
            url_esc = html.escape(url)
            urls_html += f"<a href='{url_esc}'>{protocol_esc}</a> "

        location = html.escape(mirror_cfg.get("location", "Unknown Location"))

        new += f"<b>{html.escape(name)}</b><br>\n"
        new += f"{location}\n"
        if "bandwidth" in mirror_cfg:
            new += f", {html.escape(mirror_cfg['bandwidth'])}"
        new += f"<br>\n"
        new += f"{urls_html}\n"
        new += "<br><br>\n"

    return html_str.replace(marker, new)


def replace(html):
    """ Various replacements for blog posts, to make them responsive etc.
        :param html: blog post code (already converted from markdown to HTML)
        :returns: html with replacements made """
    ret = html
    ret = grid(ret)
    ret = download_table(ret)
    ret = mirrors_list(ret)

    ret = ret.replace("[#latest release#]",
                      config.download.latest_release_title)
    return ret
