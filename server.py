import socket
import sys
import pyDes

# based on code provided on digitalocean.com
# link: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

# get the host name
host = socket.gethostname()
port = 5000

server_socket = socket.socket() # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host,port)) # bind host address and port together

print("Server is running...\n")

# configure how many client the server can listen simultaneously
server_socket.listen(1)
conn, address = server_socket.accept()  # accept new connection
print("Accept new connection from " + str(address) + "...\n")

# open the txt file containing the key and store its value in 'key'
with open("key.txt","r") as f:
        key = f.read()
# check to see if the key has 8 characters
k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

while True:
        # note: an error occurs here and closes the server if the client disconnects using 'exit' but it shouldn't be that big of a deal
        # server gets the encrypted message sent by the client
        client_message = conn.recv(1024)
        # decrypt the client's message using the key
        decrypted_message = k.decrypt(client_message).decode("utf-8")

        print("***********************") 
        print(f"Received ciphertext is: {client_message}")
        print("Received plaintext is: " + decrypted_message)
        print("***********************\n")

        message = input("Type message:\n\n") # take input from server side

        # hold the message in plaintext to have the ability to print it out later
        plaintext_message = message

        message = message.encode()
        # encrypt the server's message using the key
        encrypted_message = k.encrypt(message)
        # send the server's encrypted message to the client
        conn.send(encrypted_message)

        print("***********************")
        print("key is: " + key)
        print("Sent plaintext is: " + plaintext_message) 
        print(f"Sent ciphertext is: {encrypted_message}")
        print("***********************\n")