# Summer2021Task3
Simple Video Chat App Using Python Network Programming.

In this TASK we come to know how a basic video chat application works..😇😇

**First File to watch out FinalServer.py :**

> This File is for starting our server program which allows a client to connect through their video.
> As a first step we need to create a Socket and start listening on some port number so that any client can connect to it and starts a session.
> Next I used a external address to connect to my Mobile Cam for video capture.
> And next firstly we start receiving the client data(video) and start displaying it on our screen and we start sending our video data simultaneously as well using sendall().
> And Finally when the key 'q' is pressed the video will quit.

**Second File to watch out FinalClient.py :**

>Firstly we use the Server's IP address and Port number on which the Server started listening to establish the connection between the server and client.
>And then we continuosly start sending data to the server and receiving from it then displayed using the window.
>In both the code a buffer function is used to store our received data temporarily for sometime before displaying.
>This Simple way allows to make a video chat between two nodes.

**For More Impact :**

>If you observe the server program there is possibility of connecting one client to the server ....To improve this we can use the concept of Multi Threading in Python to establish multiple connections/sessions with various clients and can send and receive the data from them easily.

