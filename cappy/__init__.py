# -*- coding: utf-8 -*-

__title__ = 'CapPy'
__author__ = "GEONE"
__version__ = "0.0.5"
__copyright__ = "Copyright (C) 2019 Gina Taylor"
__license__ = "MIT"

from .cpy import *
try: from .cpy_cv2 import *
except ImportError: pass