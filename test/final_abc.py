#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 04:34:35 2017

@author: parth
"""

import graphviz as gv
from lxml import html

file = open("testfile.txt","r")
raw = file.read()

def traverse_tree(parent, graph, labels):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        graph.edge(parent.tag, node.tag)
        traverse_tree(node, graph, labels)
        
def traverse_tail(parent, graph, labels,count):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        global flag
        if(count>=1):
            count=count-1
        else:
            graph.edge(parent.tag, node.tag)
            traverse_tail(node, graph, labels,0)
        
def tail(subtree,name,c):
    g1 = gv.Digraph(format='png')
    g1.attr(label='Tail')
    #g1.edge_attr.update(shape='egg',arrowhead='vee', arrowsize='2')
    g1.node_attr.update(style='filled', color='skyblue')

    labels = {}     
    traverse_tail(subtree, g1, labels,c)
    #g1.view()
    g1.render('img/a'+name)
    
def traverse_prime(parent, graph, labels):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        graph.edge(parent.tag, node.tag)
        traverse_prime(node, graph, labels)

def prime(subtree,name):
    g1 = gv.Digraph(format='png')
    labels = {}     # needed to map from node to tag
    traverse_prime(subtree, g1, labels)
    #g1.view()
    g1.render('img/a'+name)
    
def traverse_head(parent, graph, labels,count):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        global flag
        if(count>=1):
            graph.edge(parent.tag, node.tag)
            traverse_head(node, graph, labels,100)
            count=count-1
        else:
            continue

def head(subtree,name,c):
    g1 = gv.Digraph(format='png')
    labels = {}     
    traverse_head(subtree, g1, labels,c)
    #g1.view()
    g1.render('img/a'+name)

#HyperTree    
g1 = gv.Digraph(format='png')
labels = {}     
html_tag = html.document_fromstring(raw)
traverse_tree(html_tag,g1,labels)
#g1.view()
g1.render('img/hypertree')

#Tail
tail(html_tag,'tail',1)

#Prime
i=0
for node in html_tag.getchildren():
    prime(node,str(i))
    i=i+1
    
#head
head(html_tag,'head',1)

