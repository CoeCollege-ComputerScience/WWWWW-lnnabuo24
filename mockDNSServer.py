#from socket import *
import datetime

from netTools import *

hosts = {}

def simpleServer():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    ip = getMyIP()
    print(ip)
    #print(datetime.datetime.now())
    s.bind((ip, 2001))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        #print(conn)

        whatToReturn = ""
        #sentData = conn.recv(1024).decode("utf-8").lower()
        sentData = receiveMessage(conn)

        splitData = sentData.split(",")
        name = splitData[0]
        claimedIP = splitData[1]

        status = ""

        if claimedIP == ip:
            status = "verified"
        else:
            status = "unsafe"

        print(status)
        if (not hosts[name]) or hosts[name]:
            # host doesnt exist
            print("host doesnt exist")



        #conn.send(whatToReturn.encode("utf-8"))
        sendMessage(conn, whatToReturn)
        conn.close()

simpleServer()