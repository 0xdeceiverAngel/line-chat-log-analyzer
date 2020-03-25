import re
import sys
from datetime import *
try:
    log = open(str(sys.argv[1]), "r",encoding="utf-8")
except:
    print("argv missing")
    sys.exit(0) 
log=log.read()
res=re.findall("Call\stime\s.*",log)
sum_sec=0
sum_min=0
sum_hour=0
all_sum=0
for i in res:
    i=i.split(' ')[2]
    # print(i)
    # try:
    if(len(i.split(':'))>=3):
        sum_sec=sum_sec+int(i.split(':')[2])
        sum_min=sum_min+int(i.split(':')[1])
        sum_hour=sum_hour+int(i.split(':')[0])
    else:
        sum_sec=sum_sec+int(i.split(':')[1])
        sum_min=sum_min+int(i.split(':')[0])
# print(sum_hour,sum_min,sum_sec)
all_sum=sum_hour*60*60+sum_min*60+sum_sec
print("call time sum",str(timedelta(seconds=all_sum)))

res=re.findall("[0-9]{2}:[0-9]{2}\s[A-Z]{2}",log) #
print("message(include call,unsent a message,photo,video,voice message and sticker)",len(res))

res=re.findall("Missed\scall",log)
print("miss call",len(res))

res=re.findall("answer",log)
print("no answer",len(res))