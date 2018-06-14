# coding=utf-8

import numpy
import pandas as pd
import os
import codecs

letter = ["a", ..., "z"]
number = ["0", ..., "9"]

def read_data():
    fileDir = os.listdir(folder_path)
    for i in fileDir:
        num = 0
        i_path = os.path.join(folder_path, i)
        myin = codecs.open(i_path, 'r', 'gbk')
        print(i)
        while True:
            #print(num)
            num += 1
            try:
                line = myin.readline().strip()
                if line == "":
                    break
                c_line = line.split('[')
                cc_line = c_line[1].split(']')
                xline = cc_line[0]
                # １　２　３　４　５　６　７　８　９　０
                xline = xline.replace('０', '0')
                xline = xline.replace('１', '1')
                xline = xline.replace('２', '2')
                xline = xline.replace('３', '3')
                xline = xline.replace('４', '4')
                xline = xline.replace('５', '5')
                xline = xline.replace('６', '6')
                xline = xline.replace('７', '7')
                xline = xline.replace('８', '8')
                xline = xline.replace('９', '9')
                for word in stopwords:
                    xline = xline.replace(word, "")
                xline = xline.replace("    ", "")
                xline = xline.replace("   ", "")
                xline = xline.replace("  ", "")
                xline = xline.replace(" ", "")
                xline = xline.replace("　", "")
                xline = xline.replace("　　", "")
                if not xline.isdigit() :
                    # print(xline)
                    myout.write(xline)
                    myout.write("\n")
            except UnicodeDecodeError as e:
                continue
            else:
                continue
        myin.close()


folder_path = "/home/hadoop/Downloads/SogouQ/newSogou"
outfile = "SougoQ.txt"
myout = open(outfile, 'w')
stopwords = []
for word in open("stopwords.txt", 'r'):
    stopwords.append(word.strip())
read_data()
myout.close()
