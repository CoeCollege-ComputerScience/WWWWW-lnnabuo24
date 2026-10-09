#from socket import *
import datetime

from netTools import *

"""
responses = {
    "who" : "I am Groot",
    "what": "Command Server 2026",
    "when"
}
"""

setResponses = {
    "who" : "I am Groot",
    "what": "Command Server 2026",
    "where": getMyIP(),
    "why": "because"
}

def getTheTime():
    return str( datetime.datetime.now().time() )

variableResponses = {
    "when": getTheTime
}

#print(variableResponses["when"]())

def simpleServer():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    ip = getMyIP()
    print(ip)
    #print(datetime.datetime.now())
    s.bind((ip, 2026))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        #print(conn)

        whatToReturn = ""
        #sentData = conn.recv(1024).decode("utf-8").lower()
        sentData = receiveMessage(conn)

        """
        if setResponses[sentData]:
            whatToReturn = setResponses[sentData]
        elif variableResponses[sentData]:
            whatToReturn = variableResponses[sentData]()
            #print("e " + whatToReturn)
        else:
            whatToReturn = "I'm sorry Dave. I can't do that"
        """


        if sentData == "who":
            whatToReturn = "I am Groot"
        elif sentData == "what":
            whatToReturn = "Command Server 2026"
        elif sentData == "when":
            whatToReturn = str( datetime.datetime.now().time() )
        elif sentData == "where":
            whatToReturn = ip
        elif sentData == "why":
            whatToReturn = "because"
        else:
            whatToReturn = "I'm sorry Dave. I can't do that"



        #conn.send(whatToReturn.encode("utf-8"))
        sendMessage(conn, whatToReturn)
        conn.close()

simpleServer()
