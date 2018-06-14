# encoding=utf-8
import jieba
import time


def jieba_data():
    for line in myin:
        if line == "\n":
            continue
        tag = 0
        line = line.strip()
        line = line.replace("    ", "")
        line = line.replace("   ", "")
        line = line.replace("  ", "")
        line = line.replace(" ", "")
        xline = jieba.cut(line)
        nxline = []
        for i in xline:
            if i not in nxline:
                nxline.append(i)
        for i in nxline:
            if i.isspace():
                continue
            myout.write(i)
            if i.isdigit() and tag == 1:
                continue
            myout.write(" ")
            if not i.isdigit():
                tag = 0
        myout.write("\n")


time_now = time.time()
localtime = time.asctime(time.localtime(time_now))
print(localtime)
infile = "SougoQ.txt"
outfile = "SougoJ2.txt"
myin = open(infile, 'r')
myout = open(outfile, 'w')
jieba_data()
myin.close()
myout.close()
cost_time = time.time()-time_now
print(cost_time)
