"""
📌 Create Live Streaming Video Chat App without voice using cv2 module of Python

SERVER side script
"""

# Importing modules
import socket         # for socket programming
import  cv2           # for image processing
import pickle         # converting a Python object into a byte stream to transport data over network
import struct         # Convert between strings and binary data.


server_socket = socket.socket()           # By default uses IPv4 address family and TCP protocol
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  <-- same as above line


host_ip = socket.gethostbyname(socket.gethostname())   # will retrieve host IP in string format
print('HOST IP:',host_ip)
port = 9999                                            # Using any random port but must be free

server_socket.bind( (host_ip,port) )                   # binding socket with ip and port
server_socket.listen(2)
print("SERVER IS LISTENING AT --> ",host_ip,port, sep=" : ")

while True:
    # Accepts request from client
    client_socket,addr = server_socket.accept()
    
    print('Recieved request from --> ',addr)
    if client_socket:
        cap = cv2.VideoCapture(0)                                              # connects to camera
        
        while(cap.isOpened()):
            ret, frame = cap.read()                                            # clicks picture
            frame_into_bytes = pickle.dumps(frame)                             # returns the byte object
            frames = struct.pack("Q",len(frame_into_bytes))+frame_into_bytes
            client_socket.sendall(frames)
            
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key  == 13:                              # 13 --> Enter key
                client_socket.close()
                break
cv2.destroyAllWindows()
cap.release()        
