import string
import random
from github import Github

f=open("SHOTUNDATA.txt",'a+')

inp=[]
out=[]
data=[]

sample=list(string.ascii_letters)

long=str(input("Enter the link to shorten: "))
short=''
new=''

f.seek(0)

data=f.readlines()


for j in range(0,len(data)):
    if j%2==1:
        out.append(data[j].strip("\n"))
    else:
        inp.append(data[j].strip("\n"))

exists=True

if long in inp:
    print(out[inp.index(long)])
elif long not in inp:
    while exists==True:
        new=''
        
        for i in range(0,8):
            new+=sample[random.randrange(0,len(sample))]
            
        short=r'https://vedant-dinkar.github.io/Shotun/'+new
        exists=short in out

        f.write(long)
        f.write("\n")
        f.write(short)
        f.write("\n")

repo.create_git_ref("refs/heads/"+new)

print(short)

f.close()
