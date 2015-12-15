#!/usr/bin/env python

import sys
import exifread

DT_ORIG = 'EXIF DateTimeOriginal'
DT_DIGI = 'EXIF DateTimeDigitized'

def handle_file(filepath):
  parts = filepath.strip().split('/')

  filename, ext = parts[-1].rsplit('.', 1)
  if not ext.lower() in ['jpg', 'mov', 'mp4']: 
    return

  f = open(line)
  all_tags = exifread.process_file(f)
  f.close()

  exif_tags = [k for k in all_tags.keys() if k.startswith('EXIF')]
  date_tags = [k for k in all_tags.keys() if k.find('DateTime') >= 0]
  for key in date_tags: 
    print "%-40s: %s" % (key, str(all_tags[key]))


if __name__ == '__main__':
  lines = sys.argv[1:] or sys.stdin

  for line in lines:
    handle_file(line)


