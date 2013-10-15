gallery
=======

Simple static gallery generator with the bootstrap blueimp theme.

Why?!
-----

I wanted something better than the archaic igal2 (in perl...), but far simpler than curator (this README has more lines than the gallery.py script).

Setup
=====

You need python2 and PIL, the Python Imaging Library.

Debian/Ubuntu:

        aptitude install python-imaging

Archlinux:

        pacman -S python2-pillow

How to
======

git clone the repository and move all files into the folder containing images for the gallery. Then execute the ./gallery.py script to generate a static *index.html* with thumbnails and responsive design. The index.html file is not self-sufficient.

All links are relative, meaning that you can move the image directory without any problem.

Technical
=========

File formats
------------

The script goes through all files into the current directory and tries to parse them with PIL. Thus, all common image file format should be supported.

Blueimp js and css
------------------

I included the blueimp files into the project as it is easier to support SSL. The blueimp bootstrap example link the http://blueimp.github.io scripts, but moving toward SSL provide the .github.com certificate. If you didn't bother using SSL you can modify the file and reduce needed files.

Theme
-----

The index.html.head page, index.html.tail page and _body_ into the code are the one to look for.

The play-pause video bug
------------------------

I will regenerate the minified version of css and js on the next version and remove video support.
