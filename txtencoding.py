#!/usr/bin/env python3

from chardet.universaldetector import UniversalDetector


class TxtEncoding:
    def __init__(self):
        # inspired by https://chardet.readthedocs.org/en/latest/usage.html#example-detecting-encodings-of-multiple-files
        self.detector = UniversalDetector()

    def detectEncoding(self, fname):
        '''Detect the encoding of file fname.
        Returns a dictionary with {'encoding', 'confidence'} fields.'''
        self.detector.reset()
        with open(fname, 'rb') as f:
            for line in f:
                self.detector.feed(line)
                if self.detector.done: break
        self.detector.close()
        return self.detector.result
        
