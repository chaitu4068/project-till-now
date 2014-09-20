#required libraries
import os
import nltk
import pylab
import csv
import networkx
import numpy 
import time

#<=======================================================================================>
def tweetFrequency():
 fl = open("xiaomi-tweet+timestamp.csv","r")
 x=object()
 timestamp = ''
 collection_of_timestamps = []
 year=0
 month=0 
 day=0
 hours=0
 minutes=0
 seconds=0
 time_tuple = []
 epoch_seconds = 0
 time_interval=raw_input('Enter the time interval')
 time_interval=int(time_interval)
 for line in fl:
  x=line.split(",")
  timestamp=x[0].strip("\"")
  print timestamp
  
  year = int(timestamp[:4])
  month = int(timestamp[5:7])
  day = int(timestamp[8:10])
  hours = int(timestamp[11:13])
  minutes = int(timestamp[14:16])
  seconds = int(timestamp[17:19])
  time_tuple = [year,month ,day , hours , minutes , seconds,0,0,0]
  #print time.mktime(time_tuple)  
  epoch_seconds = int(time.mktime(time_tuple))
  collection_of_timestamps = collection_of_timestamps + [epoch_seconds]
 #fdist = nltk.FreqDist(collection_of_timestamps)
 collection_of_timestamps = sorted(collection_of_timestamps)
 print collection_of_timestamps
 threshold=collection_of_timestamps[0] + time_interval
 time_array = [threshold]
 tweet_counts = []
 count = 0
 for item in collection_of_timestamps :
   if item < threshold :
     count=count + 1
   else :
    threshold= threshold + time_interval 
    tweet_counts =tweet_counts + [count]
    count = 0
    time_array = time_array + [threshold]
 tweet_counts = tweet_counts + [0]
 print tweet_counts , time_array      
 pylab.plot(time_array,tweet_counts) 
 pylab.title('Tweet volume vs time graph - xiaomi data' + ' interval : ' + str(time_interval))
 pylab.xlabel('time')
 pylab.ylabel('No of tweets')
 pylab.show()
#<=======================================================================================>

#<=======================================================================================>
def CMUparse():
 fl = open("xiaomi-tweets.txt","r")
 os.system("./runTagger.sh xiaomi-tweets.txt > xiaomi-tweets-tokenized.txt")
#<=======================================================================================>

#<=======================================================================================>
def ParseStats():
 fl  = open("xiaomi-tweets-tokenized.txt","r") 
 fl1 = open("entities-Xiaomi.csv","w")
 POS=[]
 tokenized_tweet = []
 named_entities = 0
 extracted_entities = []
 hashtags = 0
 atags = 0
 index = 0
 for line in fl:
  POS=line.split("\t")[1]
  tokenized_tweet = line.split("\t")[0]
  tokenized_tweet = tokenized_tweet.split(" ")
  for item in POS.split(" "):
    index = POS.index(item)
    try:
     if item == '^':
       named_entities = named_entities + 1
       extracted_entities = extracted_entities + [(tokenized_tweet[index],item)]
     if item == '#':
       hashtags = hashtags + 1
       extracted_entities = extracted_entities + [(tokenized_tweet[index],item)]
     if item == '@':
      atags = atags + 1 
      extracted_entities = extracted_entities + [(tokenized_tweet[index],item)] 	
    except Exception,e:
     print "\t\t"
 x=[named_entities,hashtags,atags]
 lab = ['Named entities','Hashtags','@ Tags']
 pylab.pie(x,labels = lab)
 pylab.title('Proportion of POS In xiaomi data after CMU parsing')
 pylab.show()
 extracted_entities=list(set(extracted_entities))
 for item in extracted_entities :
   fl1.write(item[0]+","+item[1]+"\n")
#<=======================================================================================>

#<=======================================================================================>
def totalPOSproportions():
 fl  = open("xiaomi-tweets-tokenized.txt","r") 
 POS=[]
 pos_list = []
 named_entities = 0
 hashtags = 0
 atags = 0
 for line in fl:
  POS=line.split("\t")[1]
  pos_list = pos_list + POS.split(" ")

 fdist = nltk.FreqDist(pos_list)

 x=[named_entities,hashtags,atags]
 lab = ['Named entities','Hashtags','@ Tags']
 pylab.pie(fdist.values(),labels = fdist.keys())
 pylab.title('Proportion of POS In xiaomi data after CMU parsing')
 pylab.show()
 #<=======================================================================================>

 
#function calls
tweetFrequency()
CMUparse()
ParseStats()
totalPOSproportions()
