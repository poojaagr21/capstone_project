# -*- coding: utf-8 -*-
"""capstone_final2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16vm5yIqMRxIbKygYla7uCZt6lR5iWRoM
"""

example1 = "/content/doc.txt"
file2 = open(example1, "r")
FileContent2 = file2.read()
FileContent2
import requests
from bs4 import BeautifulSoup
soup2 = BeautifulSoup(FileContent2, "html.parser")
results = soup2.find(id="reviews-target-element")

#job_elements2 = soup2.find_all("div", class_="sc-1opoey3-0 btunwM sc-1ct2r0d-1 hkwcYU")
#print(job_elements2)

#to find the ratings
review_elements = soup2.find_all("div", class_="ckodym-1 gHUzxY sc-166icl4-1 hxtUIZ")
rev = []
for review in review_elements:
  #rev =review.find('svg', {'class':"sc-14oxdvn-0 ckodym-0 brPjVo"})['data-rating'])
  rev.append(review.find('svg', {'class':"sc-14oxdvn-0 ckodym-0 brPjVo"})['data-rating'])
print(rev)

#to find the review text
rating_coment = soup2.find_all("div", class_="sc-1ct2r0d-2 hpCZUn")
com=[]
for comment in rating_coment:
  #rev =review.find('svg', {'class':"sc-14oxdvn-0 ckodym-0 brPjVo"})['data-rating'])
  com.append(comment.find("span").get_text())
  
print(com)

review_data1 = soup2.find_all("div", class_="sc-1ct2r0d-3 fEDjKu")
review_author=[]
review_source=[]
rating_date=[]
for item in review_data1:
  Number_of_spans = len(item.find_all("span"))
  author=item.find_all("span")[1].get_text()
  rating_date.append(item.find("span").get_text())
  review_author.append(author)
  if (Number_of_spans<3):
    review_source.append('No source')
  else:
    review_source.append(item.find_all("span")[2].get_text())

mainList = []

for idx, val in enumerate(review_author):
    touple=(review_author[idx], com[idx],review_source[idx],rating_date[idx])
    mainList.append(touple)
print(mainList)

import csv

# open the file in the write mode
f = open('/content/doc_exported_review1.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerows(mainList)

# close the file
f.close()