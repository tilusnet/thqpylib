#!/usr/bin/env python2
# -> eyed3 is only tested with py2

from __future__ import print_function
import eyed3
eyed3.require('0.7.5')
import logging


class Mp3Tag:
    def __init__(self, fname):
        self.tag = eyed3.load(fname).tag

    def convert(self, encoding='utf-8', backup=True, preserve_file_time=True):
        self.tag.save(encoding=encoding,
                      backup=backup,
                      preserve_file_time=preserve_file_time)

    def getLyrics(self):
        return self.tag.lyrics[0].text

    def setLogLevel(self, level):
        # affecting eyed3's log level
        elog = eyed3.utils.log
        elog.log.setLevel(level)    ## e.g. logging.DEBUG


