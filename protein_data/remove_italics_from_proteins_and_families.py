#!/usr/bin/env python3

import argparse
import shutil 
import os
import tempfile
import re


BUFFER_SIZE = 512*1024

re_i_tag = re.compile('</?i>')

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?', default='proteins_and_families.txt', action='store', help='File from where italics HTML tags will be removed in-place. A <file>.bkp backup file will be also created.')
parser.add_argument('-f','--force', default=False, action='store_true', help='Overwrite <file>.bkp')
args = vars(parser.parse_args())

bkp_file = args['file']+'.bkp'

if 'force' not in args:
    args['force'] = False

if os.path.exists(bkp_file) and not args['force']:
    raise FileExistsError('File exists: %s' % bkp_file)

shutil.copy2(args['file'],bkp_file)

with tempfile.TemporaryFile(mode='w+') as o_f:
    with open(args['file'],'a+') as i_f:
        i_f.seek(0)
        for line in i_f:
            line = re_i_tag.sub('',line)
            o_f.write(line)
        i_f.seek(0)
        i_f.truncate()
        o_f.seek(0)
        while True:
            b = o_f.read(BUFFER_SIZE)
            if not b:
                break
            i_f.write(b)









