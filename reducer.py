#!/usr/bin/python
import sys
import pandas
import mapper_project

oldKey=None
dic_list = {}
my_list = []

#Partitoner
for line in sys.stdin:
    data = line.strip().split(",","")
    if len(data) !=12:
        continue

    thisKey, thisCountry, thisPrice =data

if oldKey and oldKey != thisKey:
      if oldKey is not None:
          my_list = []
          for thiskey,oldvalue in dic_list.items():
               if data in thiskey:
                   my_list = oldkey

          for this_key,old_value in dic_list.items():
             if thisKey == this_key:
                 value = old_value

          for productlist in my_list:
              if productlist[0] in dic_list.keys():
                  total_cost= my_list(productlist[0])
                  total_cost[0]+=1
                  total_cost[1]=total_cost[1]+productlist[2]
                  dic_list[productlist[0]]=total_cost
                  print (productlist[0],total_cost,value)
              if oldKey != None:
                  print (oldKey,productlist,total_cost)
