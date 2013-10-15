#!/usr/bin/env python2
"""
clean: rm *.css *.js *.html* loading.gif *.py *~
"""

from PIL import Image
import os
import logging
import sys

class Gallery():
    def __init__(self, directory = '.'):
        self.imgnames = []
        self.directory = directory

    def get_files(self):
        self.filenames = os.listdir(self.directory)
        logging.debug("Directory files: %s" % self.filenames)

    def generate_thumbnails(self):
        counter = 0
        for name in self.filenames:
            logging.debug("Trying to open %s" % name)
            counter+= 1

            if name == "loading.gif":
                continue

            try:
                im = Image.open(name)
                self.imgnames.append(name)
                im.thumbnail( (75,75) )
                logging.debug("Saving thumb-%s" % name)
                im.save("thumb-%s" % name)
                sys.stdout.write("\r%f%%" % (counter*100.0/len(self.filenames)))
                sys.stdout.flush()
            except IOError:
                logging.debug("File %s cannot be parsed by PIL, ignoring" % name)

    def integrate_bootstrap(self):
        logging.info("Generating index.html")
        head = open("index.html.head", 'r').read()
        tail = open("index.html.tail", 'r').read()
        final = open("index.html", 'w')

        """
        <div id="links">
            <a href="images/banana.jpg" title="Banana" data-gallery>
                <img src="images/thumbnails/banana.jpg" alt="Banana">
            </a>
        </div>
        """
        body = '<div id="links">'

        for img in self.imgnames:
            body+= '<a href="%s" title="%s" data-gallery>' % (img, img.split('.')[0])
            body+= '<img src="thumb-%s" alt="%s">' % (img, img.split('.')[0])
            body+= '</a>'

        body+= '</div>'

        final.write(head)
        final.write(body)
        final.write(tail)

        logging.debug("Date written, closing index.html")
        final.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    g = Gallery()
    g.get_files()
    g.generate_thumbnails()
    g.integrate_bootstrap()
