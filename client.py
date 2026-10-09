#from socket import *
from netTools import *

def simpleClient(host):
    s = socket()
    s.connect((host, 2026))
    msg = input("prompt: ")
    #s.send(msg.encode("utf-8"))
    sendMessage(s, msg)

    #response = s.recv(1024)
    #data = response.decode("utf-8")
    data = receiveMessage(s)
    print(data)
    s.close()

#simpleClient("192.168.0.126")

#print( mockDNSLookUp("laurence") )

#simpleClient( getMyIP() )

someIP, someStatus = mockDNSLookUp( input("give me a name: ") )
if someIP != "unknown":
    simpleClient( someIP )
else:
    print("cant find them")


