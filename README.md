# CIS 3319 Lab 1 - DES

## Libraries Used
1. socket - for socket programming to simulate the server and client
2. sys - for the standard library operations
3. pyDes - to perfrom DES encryption and decryption operations

## Project Files
1. server.py
2. client.py
3. key.txt
4. testing_results.jpg
5. programdesign.txt

**server.py** - The server that the client connects to. The socket code is based on the code provided to me in the week 1 slides for this lab from digitalocean.com. The server will
wait until the client connects to it and then it will retrieve the key from key.txt and check if it has a length of 8. Then it will wait for the client to send it an encrypted
ciphertext message before decrypting the client's ciphertext message to plaintext and sending an encrypted ciphertext message back to the client. An error occurs in the server
and it closes if the client disconnects from it by sending the message 'exit' but I don't think it's really that big of deal since the client is already done sending messages 
at that point.

**client.py** - The client that connects to the server. The socket code is based on the code provided to me in the week 1 slides for this lab from digitalocean.com. The client will
connect to the server and then it will retrieve the key from key.txt and check if it has a length of 8. Then it will encrypt and send a ciphertext message to the server and wait
for the server to send an encrypted ciphertext message back which it will decrypt into plaintext. This process continues until the message 'exit' is sent by the client which will
disconnect it from the server.

**key.txt** - Holds the DES key that the server and client will both be using. The key has to be a length of 8.

**testing_results.jpg** - A screenshot of a very basic test run I did of my project.

**programdesign.txt** - The file you're looking at right now and the documentation for my project.

## How to test project
1. Open up two terminals
2. Run the server on one terminal using python server.py and the client on the other terminal using python client.py
3. Go to the client terminal first and type a message to be sent to the server. The key, plaintext message, and ciphertext message should all be printed out by the client.
4. Next, go to the server terminal and you should see the ciphertext message and decoded plaintext message from the client. 
5. Type a message to be sent to the client. The key, plaintext message, and ciphertext message should all be printed out by the server.
6. Continue this process until you want to finish testing. To disconnect from the server, type 'exit' when it's the client's turn to send a message.
