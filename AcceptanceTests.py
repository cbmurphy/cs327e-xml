#!/usr/bin/env python


# -------
# imports
# -------

import sys

from XML import xml_solve

# ----
# main
# run tests and creating Acceptance Tests
# input and out but based on 1.xml, 2.... 10.xml
# ----

instring = ''
fout = open('RunXML.out', 'w')
for i in range(1, 11):
  fname = str(i) + '.xml'
  fin = open(fname, 'r')
  xml_solve(fin, fout)
  fout.write('\n')
  fin.seek(0, 0)
  instring += fin.read() + '\n'
  fin.close()

infile = open('RunXML.in', 'w')
infile.write(instring)
fout.close()
