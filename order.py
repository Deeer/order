#! /usr/bin/python 
#coding=utf-8  
# -*- coding: UTF-8 -*-

import sys  
import string  
import os  
import random
from Carbon.Aliases import true


def readFileFunc (filePath):
	datalist = []
	the_file = open(filePath)
	handledData = the_file.read()
	handledtext = handledData.replace('\r','').replace('\n','').replace('\t','').strip()
	listData = handledtext.split(';')
	listOriginData = []
	for x in listData:
		c =x.split(":")
		datalist.append(c)
	return datalist

food_orded_list = [] # for all food list
listDicOriginData = [] # for originData  read from file
#GET MENU

listDicOriginData = readFileFunc("datafile.txt")
listOriginSoupData = readFileFunc("soup.txt")

#OPTION SETTING

while 1:
    totalCount = int(raw_input("小伙子想点几个菜啊？:\n"))
    if totalCount <= len(listDicOriginData):
        break
    else:
        print '小伙子,你吃的太多了(￢ω￢;A)'

is_needSoup = 0
is_needSoup_input = raw_input('需要汤吗:(Y OR N):\n')
print('\n好的,骚等(≧ڡ≦*)\n')
if is_needSoup_input == 'y' or is_needSoup_input == 'Y':
	is_needSoup = 1

if is_needSoup > 0:
	soupData = listOriginSoupData
	souptag = random.randint(0,len(soupData) - 1)
	list_soup = soupData[souptag]
	food_orded_list.append(list_soup)
#RANDOM
food_list = []
food_taglist = []

if is_needSoup:
	i = 1
else:
	i = 0

while i < int(totalCount):
	i = i+1
	tag = random.randint(0,len(listDicOriginData) - 1)
	if tag in food_taglist:
		i = i - 1
	else:
		food_taglist.append(tag)

#ORDERED
i = 0
while i < len(food_taglist):
	food_orded_list.append(listDicOriginData[food_taglist[i]])
	i = i + 1
dict_ordered_Data = dict(food_orded_list)
list_ordered_name = dict_ordered_Data.keys()
list_ordered_price = dict_ordered_Data.values()

#PRICE
s = sum(map(eval,list_ordered_price))

#PRINT
width = 35
price_Width = 20
item_width = width - price_Width

header_format = '%-*s%*s'
format 	      = '%-*s%*.2f'

print ('今日菜单')
print ('=' * width)
i = 0
while i < len(list_ordered_name):
	print format %(item_width,str(list_ordered_name[i]),price_Width,float(list_ordered_price[i]))
	i = i + 1
print ('=' * width)
print format % (item_width,"总价:",price_Width,s)


