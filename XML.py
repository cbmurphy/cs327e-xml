#!/usr/bin/env python

# -------
# imports
# -------

import xml.etree.ElementTree as ET
import sys

taglst = []    #list of tags from XML
nodes = []     #list of nodes corresponding to tag list in input

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

def parseTree(node):

  ''' create list of tags in XML'''
  
  taglst.append(node.tag)
  nodes.append(node)
  for x in node:
    parseTree(x)
      

def dfs_new(root, root2):

  '''
  depth first search function to check tree
  root is the occurence of the first node
  root2 is the input tree
  '''
  
  len1 = len(root)
  len2 = len(root2)

  #check if input is empty or XML is smaller than input
  if len2 == 0:
    return True
  if len1 == 0 and len2 != 0:
    return False

  #loop over tree to check for input
  i = 0
  j = 0
  while ( i < len1 and j < len2):
    if root[i].tag != root2[j].tag:
      i += 1
    else:
      if dfs_new(root[i], root2[j]):
        i += 1
        j += 1
        continue
      else:
        return False

  if i == len1 and j != len2:
    return False

  return True

# -------------
# xml_solve
# -------------

def xml_solve(r, w): 
  """ 
  read, search and print
  r is a reader
  w is a writer
  """
  global taglst
  global nodes
  xmlstr = r.read()
  root = ET.fromstring('<xml>' + xmlstr + '</xml>')

  parseTree(root[0])
  results = []
  for idx, tag in enumerate(taglst):
    if tag == root[1].tag:
      if dfs_new(nodes[idx], root[1]):
        results.append(idx+1)

  xml_print(w, results)
  taglst = []
  nodes = []

# ----
# main
# ----

if __name__ == "__main__":
  try:
    f = open("2.xml")
    xml_solve(f, sys.stdout)
  except:
    print "File missing!"
