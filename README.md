# Chaipress
A minimalist static blog-style site generator. There is just one Python script (~300 lines), nine templates, one css file, and two favicon files. You write blog posts in text files, run the script, it generates the website. You can then ftp the files to the web server or use GitHub to sync it. That is all there is.

After years of hosting my website at [WordPress](http://wordpress.com), and a brief try of Octopress+GitHub Pages, I decided to go with a home-made program. 

## What you need
1. A story you want to tell.
2. Python 3.5 ([Download](https://www.python.org/downloads/), or [Homebrew for Mac](http://brew.sh))
3. [titlecase module](https://pypi.python.org/pypi/titlecase)
4. [markdown module](https://pypi.python.org/pypi/Markdown)
5. Web server to serve the files. I am using [NearlyFreeSpeech](https://www.nearlyfreespeech.net)

## Files and Directories
* /posts/
* /templates/
* /output/
* styles.css
* process-posts.py
* favicon.gif
* favicon.ico
* wp-extract.py

Each post is a separate file located in /posts/ directory. Files ending with .md will go through Markdown -> Html translation. The file could be named anything but I name them like post-YYYY-MM-DD-unique-url-name.txt (post is in Html) or post-YYYY-MM-DD-unique-url-name.md (post is in Markdown).

The post file has four fields:

1. title (Post title)
2. name (unique name that will be used in the url, ie. example.com/YYYY/MM/DD/name)
3. date (Post date, must be in YYYY-MM-DD HH:MM:SS format, e.g. 2016-09-19 01:37:00)
4. text (Html/Markdown markup text of the post)

I have included two sample posts.

If you are migrating from WordPress, you can use wp-extract.py to import the posts from the WordPress exported xml file. I had to manually convert the text into Html so some manual effort is required. Pelican has a [WordPress importer](http://pelican.readthedocs.io/en/3.6.3/importer.html) that might take away this pain but I could not get it working on Windows.

## Generate website
1. Run `python process-posts.py`. It will read the post files, sort it in date descending order, merge the post data into the templates from /templates/ and generate rss.xml and index.html files into /output/ directory. It will also copy over the favicon.* and styles.css files into /output/.

2. FTP or use GitHub to upload /output/ into the web server.

## Make it your own
1. Edit `process-posts.py` and replace your url in line 42
2. Replace favicon.ico and favicon.gif with your own images.
3. Edit the following template files with your own details.
   1. contact-page.txt
   2. main-bottom.txt
   3. main-top.txt (change title, description, Google Analytics js, etc.)
   4. others-page.txt
   
## Quality Control
1. [W3C validated Html & RSS](https://validator.w3.org/unicorn/)

## Support
I would prefer if you email me at admin@richardhsu.net but you can tweet me [@richardhsu](https://twitter.com/richardhsu) on Twitter too.

## Why
1. The free version of WordPress has ads and I don't like them. $50/year to remove ads is more than I want to pay.

2. Design changes are limited in the free WordPress. There are many nice themes available but changes to it requires $50/year or more upgrade. I like to tweak small details.

3. A static site appeals to my minimalist, long lasting, and geeky personality.

4. I wanted to write my own blogging engine for a long time. Before Chaipress, I tried to write typical _dynamic_ web apps using C#+ASP.NET, Python+Google App Engine but didn't finish them. I bit off more than I could chew and the convenience of WordPress and other read-to-use applications was hard to resist.

5. It is called Chaipress because Chai(tea) is simple, easy-to-make, low cost, and refreshing. The _press_ is a suffix borrowed from the names of other blogging systems (WordPress, Octopress)

## Credits & Tools
Below are inspirations and tools that helped me in the design and implementation of Chaipress.

* [Daring Fireball](http://daringfireball.net) (Markdown, TitleCase, and inspiration)
* [Charles Petzold](http://www.charlespetzold.com/blog/blog.xml) (design)
* http://htmledit.squarefree.com/ (preview Html rendering)
* [MarkdownPad2](http://www.markdownpad.com) (Markdown > Html)
* http://maxdesign.com.au/css-layouts/ (My css is based on the One-column fixed-width responsive layout)
* [Pelican](http://pelican.readthedocs.io/en/3.6.3/index.html) (This got me started on Chaipress)
* [Notion and Notes](https://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html) (for telling me about [NearlyFreeSpeech](https://www.nearlyfreespeech.net/))
* [Basecamp](https://basecamp.com) (for keeping things going)
