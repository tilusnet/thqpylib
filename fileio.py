#!/usr/bin/env python3

import os

class FileIO():
    def _fname_match(self, fname, ext, ignore_ext_case):
        return fname.upper().endswith(ext.upper()) if ignore_ext_case else fname.endswith(ext)

    def getFileList(self, path, ext='', ignore_ext_case=False):
        '''NOTE: This won't work with a filename passed for 'path'.'''
        l = []
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for fname in files:
                    if not self._fname_match(fname, ext, ignore_ext_case):
                        continue
                    # append to list
                    l.append(os.path.join(root, fname))
        else:
            # 'path' must be a filename
            if self._fname_match(path, ext, ignore_ext_case):
                l.append(path)
        l.sort()
        return l
