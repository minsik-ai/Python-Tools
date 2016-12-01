import os
import base64

import pygtk
pygtk.require('2.0')
import gtk

# change directory to where the picture is
os.chdir("/user/trent/Pictures")

# open image to convert to base64
img = open("picture.jpg", "r")

# convert image to base64
img_64 = base64.b64encode(img.read())

# get the clipboard
clipboard = gtk.clipboard_get()

# copy to clipboard
clipboard.set_text(img_64)

# store clipboard data outside the application
clipboard.store()
