# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:49:37 2018

@author: Côme
""" 
#Pour utiliser cette fonction, il faut taper python json_to_csv.py rating.json rating.csv

import json, csv, sys, codecs
if sys.argv[1] is not None and sys.argv[2] is not None :
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]

    types_of_encoding = ["utf8", "cp1252", "cp850"]

    for encoding_type in types_of_encoding:
        inputFile = codecs.open(fileInput, encoding = encoding_type, errors ='replace')
        outputFile = codecs.open(fileOutput, 'w', encoding="utf-8")
        data= json.load(inputFile)
        inputFile.close()
    
        output = csv.writer(outputFile, delimiter=';')
    
        output.writerow(data[0].keys())
    
        for row in data :
            output.writerow(row.values())