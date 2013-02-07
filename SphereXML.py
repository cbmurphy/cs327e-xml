#!/usr/bin/env python

import xml.etree.ElementTree as ET

taglst = []    #list of tags
nodes = []     #list of nodes corresponding to tag list

inputlst = []  

def parseTree(node):
  taglst.append(node.tag)
  nodes.append(node)
  for x in node:
    parseTree(x)

def parseInput(node):
  inputlst.append(node.tag)
  for x in node:
    parseInput(x)

def traverseTree(node1, idx):
  for child in node1:
    if child.tag == inputlst[idx]:
      #print "Found child: " + str(child.tag)
      if idx == len(inputlst) - 1:
        return True
      return traverseTree(child, idx + 1)
  return False

# -------------
# xml_print
# -------------

def xml_print(w, results):
  """ 
  print the results
  w is a writer
  results is a list containing matches
  """
  w.write(str(len(results)) + '\n')
  for num in results:
    w.write(str(num) + '\n')


# -------------
# xml_solve
# -------------

def xml_solve(r, w): 
  """ 
  read, search and print
  r is a reader
  w is a writer
  """

  xmlstr = r.read()
  root = ET.fromstring('<xml>' + xmlstr + '</xml>')

  for idx, child  in enumerate(root):
    if idx == 0:
      parseTree(child)
    else:
      parseInput(child)

  results = []
  for idx, tag in enumerate(taglst):
    if tag == inputlst[0]:
      if traverseTree(nodes[idx], 1):
        results.append(idx+1)

  xml_print(w, results)


# code bellow goes to RunXML.py
import sys

xml_solve(sys.stdin, sys.stdout)
