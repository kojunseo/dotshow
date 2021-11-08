# __init__.py
# Copyright (C) 2019 (gnyontu39@gmail.com) and contributors
#

import inspect
import os
import sys

__version__ = '0.0.3'

from .matching import change_img as thumshow

__all__ = [thumshow,]