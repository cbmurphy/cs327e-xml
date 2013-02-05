#!/usr/bin/env python

import xml.etree.ElementTree as ET

taglst = []    #list of tags
nodes = []     #list of nodes corresponding to tag list

inputlst = []  

tree = ET.parse('xml.xml')
inpt = ET.parse('xml2.xml')

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
    
root1 = tree.getroot()
root2 = inpt.getroot()

parseTree(root1)
parseInput(root2)

results = []
for idx, tag in enumerate(taglst):
  if tag == inputlst[0]:
    if traverseTree(nodes[idx], 1):
      results.append(idx+1)

print len(results)
for num in results:
  print num
