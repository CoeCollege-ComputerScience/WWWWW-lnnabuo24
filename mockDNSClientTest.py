from netTools import *

# just to make sure the mock dns lookup works

def simpleClient(host):
    s = socket()
    s.connect((host, 2001))
    msg = input("name: ") + "," + getMyIP()
    #s.send(msg.encode("utf-8"))
    sendMessage(s, msg)

    #response = s.recv(1024)
    #data = response.decode("utf-8")
    data = receiveMessage(s)
    print(data)

    status = data[3:]
    if status == "unsafe":
        raise ConnectionError("unsafe IP")
    else:
        nextMsg = input("(either ok or where [name]): ")
        sendMessage(s, nextMsg)

        if nextMsg != "ok":
            result = receiveMessage(s)
            print(result)

    s.close()

simpleClient("192.168.0.225")
#simpleClient("192.168.0.43")
#simpleClient(getMyIP())