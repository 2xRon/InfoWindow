#!/usr/bin/env python3

import logging
import os
from driver import epd7in5_V2
from PIL import Image

# Setup Logging -  change to logging.DEBUG if you are having issues.
logging.basicConfig(level=logging.INFO)
logging.info("Screen saver starting")


def main():
    epd = epd7in5_V2.EPD()
    epd.init()

    images = ["black.png", "white.png"]
    for image in images:
        logging.info("Display %s" % image)
        image_data = Image.open(os.path.join("resources", image))
        epd.display(epd.getbuffer(image_data))

    epd.sleep()
    logging.info("Screen saver finished")


if __name__ == '__main__':
    main()
