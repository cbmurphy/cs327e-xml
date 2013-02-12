#!/usr/bin/env python

"""
To test the program:
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import * 

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
  # -------
  # print 
  # -------

  def test_print_1(self):
    w = StringIO.StringIO()
    res = [1]
    xml_print(w, res)
    self.assert_(w.getvalue() == "1\n1\n")

  def test_print_2(self):
    w = StringIO.StringIO()
    res = []
    xml_print(w, res)
    self.assert_(w.getvalue() == "0\n")

  def test_print_3(self):
    w = StringIO.StringIO()
    res = [1, 2, 3]
    xml_print(w, res)
    self.assert_(w.getvalue() == "3\n1\n2\n3\n")

  # -----------
  # parseTree 
  # -----------

  def test_parseTree_1(self):
    self.assert_(0)

  def test_parseTree_2(self):
    self.assert_(0)

  def test_parseTree_3(self):
    self.assert_(0)

  # --------
  # dfs_new 
  # --------

  def test_dfs_new_1(self):
    self.assert_(0)

  def test_dfs_new_2(self):
    self.assert_(0)

  def test_dfs_new_3(self):
    self.assert_(0)

  # -----
  # solve
  # -----

  def test_solve_1(self):
    self.assert_(0)

  def test_solve_2(self):
    self.assert_(0)

  def test_solve_3(self):
    self.assert_(0)
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
