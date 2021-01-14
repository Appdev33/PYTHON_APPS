import gzip
import re

f = gzip.open('title.basics.tsv.gz', 'rb')
list = []
for i in f.readlines():
    print(i.decode("utf-8").upper().replace('\\n','').split('\t')[0])




#with gzip.open('title.basics.tsv.gz', 'rb') as f:
    #head = [next(f) for x in range(10)]

    #p = re.compile("^tt\d+$")
    #print(p.findall(f.readlines))
