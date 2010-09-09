"""Default settings for the application.

"""
import os

SERVER_SOFTWARE = os.environ['SERVER_SOFTWARE'].split('/')[0]
if SERVER_SOFTWARE == 'Development':
	DEBUG = True
else:
	DEBUG = False

THUMB_SIZES = [32, 48, 64, 72, 75, 104, 144, 150, 160]
THUMB_SIZE_DEFAULT = 72
THUMB_CROPPED_DEFAULT = True

FULL_SIZES = [94, 110, 128, 200, 220, 288, 320, 400, 512, 576, 640, 720, 800, 912, 1024, 1152, 1280, 1440, 1600]
FULL_SIZE_DEFAULT = 576

HOMEPAGE_SIZE_DEFAULT = 800

MEMCACHE_ENABLED = True
MEMCACHE_EXPIRATION = 3600 # 1 hour cache
MEMCACHE_PHOTO_EXPIRATION = MEMCACHE_EXPIRATION * 48 # 48 hour photo cache

PHOTO_BACKEND_PICASA = 1
PHOTO_BACKEND_FLICKR = 2
PHOTO_BACKENDS = [PHOTO_BACKEND_PICASA, PHOTO_BACKEND_FLICKR, ]