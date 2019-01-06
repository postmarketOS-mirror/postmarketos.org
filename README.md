# postmarketos.org

## Dev

### Python Requirements Setup

Python 3.4+ is supported. Install all requirements, preferably within a virtualenv:

```shell
$ python -m venv .venv
$ source .venv/bin/activate
(venv)$ pip install -r requirements.txt
```

### New Blog Content

Blog content is written in markdown format with metadata in the file header. Filename syntax is `yyyy-mm-dd-slug.md`.

```shell
$ cat >content/blog/2017-12-31-happy-new-year.md << EOF
> ---
> title: Happy New Year!
> ---
>
> This is a *markdown* **formatted** post.
> EOF
```

### Writing responsive content

Use the following custom tags to create responsive sections in the blog posts:
* `[#grid side#]`
* `[#grid text#]`
* `[#grid bottom#]`
* `[#grid end#]`

Using any tag except for "end" will encapsulate the following markdown code in the grid area of the same name. If the grid was not opened yet, it will be opened with the first tag. The "end" tag closes the grid.

The grid layout looks like this, in desktop mode:

|text|(20px free space)|side|
|bottom|(20px free space)|side|

...and with a lower screen width (mobile phones etc.):

|side|
|text|
|bottom|

Use the responsive mode tools of your browser to check if it works as expected. For usage examples, look at the existing blog posts and the grid-related code in `static/css/page.css`. This feature is implemented in `page.py`.

### Dev Server

Run the dev server during local development, changes are auto reloaded:

```shell
(venv)$ FLASK_DEBUG=1 FLASK_APP=app.py flask run
```

### Build

To run a static site build, run:

```shell
(venv)$ python freeze.py
```

This will generate a static version in `docs/`. Any manual changes to the `docs/` directory will be overridden in the next build.

Note that the `docs/` directory is ignored and not versioned.


### Upgrading requirements.txt

```shell
(venv)$ pip install pip-upgrader
(venv)$ pip-upgrade
```
