from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    #recipient = "<mn3585@nyu.edu>"
    #sender = "<mn907@georgetoen.edu>"
    #username = "mn907"
    #password = 'IncomeLookWellOysterLedge'
    #mailserver = "smtp.gmail.com"
    #port = 587

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)  # You can use this print statement to validate return codes from the server.

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM: <mn3585.nyu.edu>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    recipientAccount = "RCPT TO: <naznin247@gmail.com>\r\n"
    clientSocket.send(recipientAccount.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCom = "DATA\r\n"
    clientSocket.send(dataCom.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCom = "QUIT\r\n"
    clientSocket.send(quitCom.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    clientSocket.close()
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
