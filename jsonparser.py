# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:59:19 2018

@author: Darragh
"""

import json

with open('coords_escaped_postcode.json', 'r') as f: 
    parsed_json = json.load(f)
    
text = []
for postcode in parsed_json:
    #print(postcode) # gives all keys
    
   # print(parsed_json[postcode][0]["text"]) # gives text of everything
    text.append(parsed_json[postcode][0]["text"]).encode('utf-8')

text = str(text)

with open('newlog.txt','w') as f:
    f.write(text.encode('utf-8'))

    #text = parsed_json[postcode][0]["text"]
 
    
         