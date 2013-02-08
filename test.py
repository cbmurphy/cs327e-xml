#!/usr/bin/env python

import xml.etree.ElementTree as ET

taglst = []    #list of tags
nodes = []     #list of nodes corresponding to tag list

#inputlst = []  

def parseTree(node):
  taglst.append(node.tag)
  nodes.append(node)
  for x in node:
    parseTree(x)

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

def tags(node):
  return node.tag

def dfs(root, sterm):
  if len(root) == 0 and len(sterm) != 0:
    return False
  for childterm in sorted(sterm, key = tags):
    for idx, child in enumerate (sorted(root, key = tags)):
      if child.tag < childterm.tag:
        if idx < len(root) - 1:
          continue
        else:
          return False
      elif child.tag == childterm.tag:
        if dfs(child, childterm):
          break
        else:
          return False
      else:
        return False
  return True
      
    
def dfs_new(root, sterm):
  l1 = len(root)
  l2 = len(sterm)

  if l2 == 0:
    return True
  if l1 == 0 and l2 != 0:
    return False
  i = 0
  j = 0
  children1 = sorted(root, key = tags)
  children2 = sorted(sterm, key = tags)
  while( i < l1 and j < l2):
    if children1[i].tag < children2[j].tag:
      i += 1
    elif children1[i].tag == children2[j].tag:
      if dfs_new(children1[i], children2[j]):
        i += 1
        j += 1
        continue
      else:
        return False
    else:
      return False

  if i == l1 and j != l2:
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

  xmlstr = r.read()
  root = ET.fromstring('<xml>' + xmlstr + '</xml>')

  for idx, child  in enumerate(root):
    if idx == 0:
      parseTree(child)
      del xmlstr
    elif idx == 1:
      results = []
      for idx, tag in enumerate(taglst):
        if tag == child.tag: 
          if dfs_new(nodes[idx], child):
            results.append(idx+1)

  xml_print(w, results)




# -------
# imports
# -------

import sys


# ----
# main
# ----

xml_solve(sys.stdin, sys.stdout)
