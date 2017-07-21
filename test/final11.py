#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:55:27 2017

@author: parth
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 07:13:36 2017

@author: parth
"""
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import graphviz as gv
from lxml import html

def hyper_tree(parent):
    g1 = gv.Digraph(format='png')
    g1.attr(label='Hyper Tree')
    g1.node_attr.update(style='filled', color='skyblue')
    labels = {}     
    traverse_tree(parent, g1, labels)
    g1.render('img/hypertree')
    g1.view()

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
        
def tail(subtree):
    i=0
    for node in subtree.getchildren():
        g1 = gv.Digraph(format='png')
        g1.attr(label='Tail_'+str(i))
        #g1.edge_attr.update(shape='egg',arrowhead='vee', arrowsize='2')
        g1.node_attr.update(style='filled', color='skyblue')
        labels = {}     
        traverse_tail(subtree, g1, labels,i+1)
        g1.render('img/tail'+str(i))
        g1.view()
        i=i+1

def prime(html_tag):
    i=0
    for node in html_tag.getchildren():
        prime_p(node,str(1))
        break;
    #i=i+1

def prime_p(subtree,name):
    g1 = gv.Digraph(format='png')
    g1.attr(label='Prime_'+name)
    g1.node_attr.update(style='filled', color='skyblue')
    labels = {}     # needed to map from node to tag
    traverse_prime(subtree, g1, labels)
    g1.render('img/prime_'+name)
    g1.view()
    
def traverse_prime(parent, graph, labels):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        graph.edge(parent.tag, node.tag)
        traverse_prime(node, graph, labels)

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

def head(subtree):
    i=0
    for node in subtree.getchildren():
        g1 = gv.Digraph(format='png')
        g1.attr(label='Head_'+str(i))
        g1.node_attr.update(style='filled', color='skyblue')
        labels = {}     
        traverse_head(subtree, g1, labels,i+1)
        g1.render('img/head'+str(i))
        g1.view()
        i=i+1
    
def imp(raw):
    root1=Tk()
    root1.title( "Tree Operation")
    root1.attributes
    html_tag = html.document_fromstring(raw)
    b1 = Button(root1, text = "Prime (')   ", command = lambda:prime(html_tag),font=("Times", "18"))
    b1.place(x=30,y=130)
    b2 = Button(root1, text = "Tail (!)      ", command = lambda:tail(html_tag),font=("Times", "18"))
    b2.place(x=30,y=50)
    b3 = Button(root1, text = "Head (&)  ", command =  lambda:head(html_tag),font=("Times", "18"))
    b3.place(x=30,y=90)
    b4 = Button(root1, text = "Hyper Tree", command =  lambda:hyper_tree(html_tag),font=("Times", "18"))
    b4.place(x=30,y=10)
    root1.mainloop()
    
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    try:
        with open(name,'r') as UseFile:
           raw = UseFile.read()
           imp(raw)
    except:
        print("No file exists")


root = Tk()
Title = root.title( "Web Data Management")
root.geometry("400x100")

label = ttk.Label(root, text ="Data Model Generation",foreground="black",font=("Times", "24", "bold italic"))
label.pack()
B = Button(root, text = "Select an File", command = OpenFile,font=("Times", "18"))
B.place(x=125,y=50)
root.mainloop()
