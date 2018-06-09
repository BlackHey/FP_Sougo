# coding=utf-8

import numpy
import pandas as pd
import os
import codecs

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
                myout.write(cc_line[0])
                myout.write("\n")
                #print(cc_line[0])
            except UnicodeDecodeError as e:
                continue
            else:
                continue
        myin.close()


folder_path = "/home/hadoop/Downloads/SogouQ/newSogou"
outfile = "SougoQ.txt"
myout = open(outfile, 'w')
read_data()
myout.close()
