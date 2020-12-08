#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import gi
from gi.module import get_introspection_module
gi.require_version('GdkPixbuf', '2.0') 
from gi.repository import GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf, Colorspace 
import numpy as np

def numpy2pb(numpy_array):
    assert numpy_array.dtype == np.uint8
    height, width, channels = numpy_array.shape
    assert channels == 4
    res = Pixbuf.new_from_data(
        numpy_array.tobytes(), 
        Colorspace.RGB, 
        True,
        8, 
        width, height, width * channels, None, None)
    return res


def save_pixbuf(pixbuf, filename):
    """Save pixbuf to a named file (compatibility wrapper)
    :param GdkPixbuf.Pixbuf pixbuf: the pixbuf to save
    :param unicode filename: file path to save as
    :param str type: type to save as: 'jpeg'/'png'/...
    """
    with open(filename, 'wb') as fp:
        print("A"*20)
        result = pixbuf.save_to_callbackv(
            lambda buf, size, data: fp.write(buf) or True,  # save_func
            fp,  # user_data
            'png',
            [],
            [],
        )
        print("B"*20)


def reproduce_bug():
    print("reproduce_bug()")
    canvas = np.load('./numpy2pb.npy')
    pb2 = numpy2pb(canvas)
    save_pixbuf(pb2, "./numpy2pb.png")
    pass

reproduce_bug()

