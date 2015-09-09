# python script to add format to ".sql"
# -*- coding: utf-8 -*-

import sys
import glob

for f in glob.glob('*.sql'):
    for line in open(f,'r'):
        sys.stdout = open('importdata.sql', 'a')
        print line[:-1]
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        open('importdata.sql', 'r').read()
        print line[:-1]
