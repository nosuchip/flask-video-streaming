# -*- coding: utf-8 -*-

import pygame, pygame.camera
from cStringIO import StringIO
from PIL import Image

class PygameCamera(object):
    def __init__(self):
        pygame.camera.init()
        cameras = pygame.camera.list_cameras()
        if not cameras:
            raise ValueError('No cameras found')
        self.cam = pygame.camera.Camera(cameras[0], (640,480))
        self.cam.start()

    def __del__(self):
        self.cam.stop()

    def get_frame(self):
        surf = self.cam.get_image()
        data = pygame.image.tostring(surf, 'RGBA')
        img = Image.frombytes('RGBA', (640,480), data)
        zdata = StringIO()
        img.save(zdata, 'JPEG')
        return zdata.getvalue()
