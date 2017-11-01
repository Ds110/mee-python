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
        
            
        
