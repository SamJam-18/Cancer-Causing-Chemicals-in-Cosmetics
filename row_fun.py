import warnings
warnings.filterwarnings('ignore')

from pymongo import MongoClient
import pprint
import numpy as np
import copy
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import re


ulta_data = pd.DataFrame({'product_name': [1] , 'product_num':[1], 'mfg_name':[1], 'product_type':[1], 'price':[1], 'ingredients':[1]})


client = MongoClient('localhost', 27017)
db = client.metroid
pages = db.pages



def product_name(site):
  name =(site.find('div', class_ = "ProductMainSection__productName"))
  product = name.text.strip()
  return product

def mfg_name(site):
  mfg_name =(site.find('div', class_ = "ProductMainSection__brandName"))
  brand = mfg_name.text.strip()
  return brand

def product_num(site):
  product_num =(site.find('div', class_ = "ProductMainSection__itemNumber"))
  item_num = int(product_num.text.strip().split('|')[1].replace('Item ',''))
  return item_num

def product_type(site):
  list_type = []
  for tag in site.find("li"):
    list_type.append(tag.text)
  product_ty = list_type[3]
  return product_ty

def price(site):
  price =(site.find('div', class_ = "ProductPricingPanel"))
  product_price = float(price.text.strip().replace('Price$', ''))
  return product_price

def ingredients_(site):
  ing =(site.find('div', class_ = "ProductDetail__ingredients"))
  product_ing = ing.text.strip().split(',')
  return product_ing


def run_url(list_url):
  k = []
  for page in list_url:
    r = requests.get(page)
    pages.insert_one({'html': r.content})
    soup = BeautifulSoup(r.content, "html")

    d = pd.Series[a, b, c, d, e, f]
    ulta_data.append(d, ignore_index=True)


  return ulta_data



print (run_url(['https://www.ulta.com/shape-tape-concealer?productId=xlsImpprod14251035','https://www.ulta.com/born-this-way-undetectable-medium-full-coverage-foundation?productId=xlsImpprod12621017' ]))



