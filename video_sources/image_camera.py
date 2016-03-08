# -*- coding: utf-8 -*-

import os.path
from time import time

class ImageCamera(object):
    def __init__(self):
        root = os.path.join(os.path.dirname(__file__), '..', 'static', 'img')

        self.frames = [open(os.path.join(root, '1{}.jpg'.format(f)), 'rb').read() for f in xrange(1, 7)]

    def get_frame(self):
        return self.frames[int(time()) % 6]
