#required libraries
import os
import nltk
import pylab
import wikipedia
import networkx as nx

#<=======================================================================================>
def readTweet(): #takes on top 10  hashtags and @ tags
 fl = open("xiaomi.csv","r")
 x=object()
 tweet = ''
 lst = []
 for line in fl:
   x=line.split(",")
   if len(x) > 3:
     tweet = x[-3]
     tweet = tweet.split(" ")
   for items in tweet:
     if items.startswith("#") or items.startswith("@"):
        print items  
        lst = lst + [items]
 fdist=nltk.FreqDist(lst)
 print fdist
 g=nx.Graph()
 g.add_node("Xiaomi")
 g.add_nodes_from(fdist.keys()[:10])
 nodes = []
 for node in fdist.keys()[:10] :
  print node
  g.add_edge("Xiaomi",node)
  try :
   nodes = wikipedia.search(node)[:2]
  except Exception,e :
    print str(e)
  if len(nodes) >= 2 :
   g.add_nodes_from(nodes)
   g.add_edge(node,nodes[0])
   g.add_edge(node,nodes[1])
 nx.draw(g)
 pylab.show()
 
#<=======================================================================================>

#this is the function call
readTweet()
