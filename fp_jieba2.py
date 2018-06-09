# encoding=utf-8
import jieba
import time


def jieba_data():
    for line in myin:
        if line == "":
            tag = 1
        else:
            tag = 0
            xline = jieba.cut(line.strip())
            for i in xline:
                for j in stopwords:
                    if i.find(j) != -1:
                        tag = 1
                        break
        if tag == 0:
            myout.write("  ".join(xline))
            myout.write("\n")


time_now = time.time()
infile = "SougoQ.txt"
outfile = "SougoJ2.txt"
myin = open(infile, 'r')
myout = open(outfile, 'w')
stopwords = []
for word in open('stopwords.txt', 'r'):
    stopwords.append(word.strip())
jieba_data()
myin.close()
myout.close()
cost_time = time.time()-time_now
print(cost_time)
