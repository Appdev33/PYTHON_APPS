import gzip
import re

f = gzip.open('title.basics.tsv.gz', 'rb')
list = []
cnt=0
for i in f.readlines():
    #print(i.decode("utf-8").upper()[1])
    # print(i.decode("utf-8").upper().replace('\\n','').split('\t')[1])
    Genre = i.decode("utf-8").upper().replace('\\n','').split('\t')[1]

    if(Genre=='MOVIE'):
        print(i.decode("utf-8").upper().replace('\\n','').split('\t'))
        cnt+=1
        print(cnt)




# with gzip.open('title.basics.tsv.gz', 'rb') as f:
#     head = [next(f) for x in range(10)]
#
#     p = re.compile("^tt\d+$")
#     print(p.findall(f.readlines))
