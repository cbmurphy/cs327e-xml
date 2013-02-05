#!/usr/bin/env python

import xml.etree.ElementTree as ET

'''
tree = ET.parse('xml.xml')
root = tree.getroot()
print root.tag
for child in root:
  print "\t" + str(child.tag)
  for child2 in child:
    print "\t\t" + (child2.tag)
'''

lst = []
nodes = []

tree = ET.parse('xml.xml')
inpt = ET.parse('xml2.xml')

def parseTree(node):
  lst.append(node.tag)
  nodes.append(node)
  for x in node:
    parseTree(x)

inputlst = []
def parseInput(node):
  inputlst.append(node.tag)
  for x in node:
    parseInput(x)




def traverseTree(node1, idx):
  for child in node1:
    if child.tag == inputlst[idx]:
      print "Found child: " + str(child.tag)
      if idx == len(inputlst) - 1:
        return True
      return traverseTree(child, idx + 1)
  return False
    

root1 = tree.getroot()
root2 = inpt.getroot()

parseTree(root1)
parseInput(root2)

print lst
print nodes
print inputlst

i = 0
results = []
for tag in lst:
  if tag == inputlst[0]:
    print i+1
    if traverseTree(nodes[i], 1):
      results.append(i+1)
    i += 1


print len(results)
print results
    
    
