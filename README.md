This is a repository for storing web-pages of ThRaSH seminars. Its structure is:

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