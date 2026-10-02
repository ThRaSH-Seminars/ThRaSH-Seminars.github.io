This is a repository for storing web-pages of ThRaSH seminars. 

## New style

Since Autumn 2026, we offer future organizers to use a new template with [Bootstrap](https://getbootstrap.com/) for modern looks and Web-plasticity support, and [Katex](https://katex.org/) to write mathematics in the abstracts. The instructions is pretty much the same as below except files have the suffixes `modern` attached to them. Also the website is a single page and we no longer need to link to `pre/index.html` anymore (but you still need to update that file, in case future organizers prefer the old style below).

The file list is quite similar: 
- `index.html` &mdash; the single webpage of the seminar, visible at https://thrash-seminars.github.io/.
- `template-modern.html` &mdash; a template for future organizers to copy and make it the new `index.html`.
- `thrash-modern-autumn.css` and `thrash-modern-spring.css` &mdash; style sheet for Autumn and Spring themes respectively. If you dislike those, you can also make your own.
- `pre` folder &mdash; contains sub-folders with web-pages of the previous editions. Again, when starting organizing a new edition, move the old `index.html` here to its own folder and correct the CSS path as instructed.

The template was written by github user d2cmath, with a little help from OpenAI's [hallucinating machine](https://chatgpt.com/). It is free and wild, and user d2cmath will take no responsibility in case of misuses or damage to your devices by the template.

## Old style

Its structure is:

- `index.html` &mdash; the current web-page of the seminar, which you can access at https://thrash-seminars.github.io/
- `template.html` &mdash; a template of an empty page (from which you can create a new seminar series page)
- `thrash.css` &mdash; css file, which contains all necessary classes for this template
- `pre` folder &mdash; contains sub-folders with web-pages of the previous series and file `index.html` to navigate through them.

This is a very minimalistic template, in which each page has a menu in the top with only two items: **Home** and **Previous**. **Home** links to the webpage of the current series, that is, to https://thrash-seminars.github.io/, and **Previous** links to the page `pre/index.html`, which helps to navigate through the pages of the previous series.

If you are a new organizer of the series, you should do the following actions:

- Create a folder in `pre` for the previous series, e.g., `autumn23-spring24` and copy the current `index.html` file there.
- Change the link to css in the `<head>` of the copied file. Replace ```<link rel="stylesheet" href="thrash.css">``` with ```<link rel="stylesheet" href="../../thrash.css">```
- Replace `index.html` with `template.html` and add your content there.

This template was written by Denis Antipov, and you can use it as you want without any constraints.
