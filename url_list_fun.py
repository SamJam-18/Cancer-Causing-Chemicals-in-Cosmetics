from pymongo import MongoClient
import pprint

import copy
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import re

import time

import warnings
warnings.filterwarnings('ignore')

def request(website):
  r = requests.get(website)
  client = MongoClient('localhost', 27017)
  db = client.metroid
  pages = db.pages
  pages.insert_one({'html': r.content})
  soup = (BeautifulSoup(r.content, "html.parser"))
  return soup

def get_url_pgs (ran, type):
  page_list =[]
  lsts = []
  for i in range (0, ran, 96):
    url = 'https://www.ulta.com/' + type + '?N=26y3&No='+ str(i) +'&Nrpp=96'
    page_list.append(url)


  for web in page_list:
    page = request(web)
    data = page.findAll(class_ = 'prod-desc')
    for div in data:
      links = div.findAll('a')
      for a in links:
        lsts.append("http://www.ulta.com" + a['href'])
    time.sleep(5)

  return (list(dict.fromkeys(lsts)))





#face
#face_ = get_url_pgs(1729, 'makeup-face')

#eyes
#eyes_ = get_url_pgs(1983, 'makeup-eyes')

#lips
#lips_ = get_url_pgs(861, 'makeup-lips')

#Cleansers
#clean_ = get_url_pgs(1019, 'skin-care-cleansers')

#Moisturizers
#moist_ = get_url_pgs(1235, 'skin-care-moisturizers')

#Treatment/serums
#serums_ = get_url_pgs(1206, 'skin-care-serums')

#eyecream
#eyecream_ = get_url_pgs(320, 'skin-care-eye-treatments')


#suncare
#sun_ = get_url_pgs(1268, 'skin-care-suncare')


def full_list(lst_all):
  full_url_lst = []

  for lst1 in lst_all:
    for elem in lst1:
      full_url_lst.append(elem)
  return full_url_lst




#print (len(full_list([face_, eyes_, lips_, clean_, moist_, serums_, eyecream_, sun_ ])))

