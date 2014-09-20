#this module is for cleaning the data of non english tweets
#and outoutting just tweet + timestamp

#input -> csv file directly from sysomos
#output -> csv file with tweets + timestamp 

#required libraries
import os
import nltk
import networkx as nx
import pylab
import language_detector as ld

#<=======================================================================================>
def dataCleaning():
 fl = open("xiaomi.csv","r")
 fl1 = open("xiaomi-tweet+timestamp.csv","w")
 fl2 = open("xioami-tweets.txt","w") 
 tweet = ''
 timestamp = ''
 x=object()
 for line in fl:
  x=line.split(",")
  if len(x) > 3:
    tweet = x[-3]
    timestamp = x[2]
  print tweet, timestamp 
  if ld.findLanguage(tweet)=='english' : 
   fl1.write(timestamp+","+tweet+"\n")
   fl2.write(tweet+"\n")
 
#<=======================================================================================>

#this is the function call
dataCleaning()
