# Copyright (c) 2017, Daisuke Saito (Ds110)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
from browser import document, ajax

def on_complete(req):
   if req.status==200 or req.status==0:
       print(req.text)
   else:
       print("error "+req.text)

def mee_connection(url):
    req = ajax.ajax()
    req.bind('complete',on_complete)
    req.open('GET',url,False)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send()

def placeBlock(slotNum = 1, direction="back"):
    url = "http://localhost:8080/place"
    qs = "?slotNum=" + str(slotNum)+"&direction="+ direction
    mee_connection(url+qs)

def moveAgent(direction="forward"):
    url = "http://localhost:8080/move"
    qs = "?direction=" + direction
    mee_connection(url+qs)

def turnAgent(direction="left"):
    url = "http://localhost:8080/turn"
    qs = "?direction=" + direction
    mee_connection(url+qs)

def tpAgent():    
    url = "http://localhost:8080/tptoplayer"
    for i in range(3):
        moveAgent()

    mee_connection(url)
        
            
        
