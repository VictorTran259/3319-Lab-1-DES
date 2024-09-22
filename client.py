import socket
import sys
import pyDes

# based on code provided on digitalocean.com
# link: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

host = socket.gethostname() # as both code is running on same pc
port = 5000 # socket server port number

client_socket = socket.socket() # instantiate
client_socket.connect((host,port)) # connect to the server

# open the txt file containing the key and store it in 'key'
with open("key.txt","r") as f:
    key = f.read()
# check to see if the key has 8 characters
k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

message = input("Type message:\n\n") # take input from client side

# the client can end the connection to the server by typing 'exit'
while message.lower().strip() != 'exit':
    # hold the message in plaintext to have the ability to print it out later
    plaintext_message = message

    # encode the message as a byte object
    message = message.encode()
    # encrypt the message using the key
    encrypted_message = k.encrypt(message)
    # send the client's encrypted message to the server
    client_socket.send(encrypted_message)
    
    print("***********************")
    print("key is: " + key)
    print("Sent plaintext is: " + plaintext_message) 
    print(f"Sent ciphertext is: {encrypted_message}")
    print("***********************\n")

    # client gets the encrypted message sent by the server
    server_message = client_socket.recv(1024)
    # decrypt the server's message using the key
    decrypted_message = k.decrypt(server_message).decode("utf-8")

    print("***********************") 
    print(f"received ciphertext is: {server_message}")
    print("received plaintext is: " + decrypted_message)
    print("***********************\n")

    message = input("Type message:\n\n") # again take input from client side

client_socket.close()  # close the connection