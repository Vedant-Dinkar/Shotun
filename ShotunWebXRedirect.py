from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

g=open("SHOTUNDATA.txt",'r+')

dat=g.readlines()
c=[]

for j in range(0,len(dat)):
    c.append(dat[j].strip("\n"))

short=c[c.index(short)-1]

def catch_all(path):
    return redirect(short, code=302)

if __name__ == '__main__':
    app.run()
