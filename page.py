# Copyright 2021 Oliver Smith
# SPDX-License-Identifier: GPL-3.0-or-later

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
        return


def replace(html):
    """ Various replacements for blog posts, to make them responsive etc.
        :param html: blog post code (already converted from markdown to HTML)
        :returns: html with replacements made """
    ret = grid(html)
    ret = download_table(html)
    return ret
