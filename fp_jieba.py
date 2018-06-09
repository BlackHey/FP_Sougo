# encoding=utf-8
import jieba
import time




def jieba_data():
    for line in myin:
        xline = jieba.cut(line)
        sline = ""
        tag = 0
        for i in xline:
            if i not in stopwords:
                sline += i
                sline += " "
            else:
                tag = 1
                break
        if tag == 0:
            myout.write(sline)
            myout.write("\n")
        # myout.write("  ".join(xline))
        #myout.write("\n")


time_now = time.time()
infile = "SougoQ.txt"
outfile = "SougoJ.txt"
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
