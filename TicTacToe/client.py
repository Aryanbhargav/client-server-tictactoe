import socket
import sys
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='localhost'
port = 9991
c.connect((host,port))

board = [['*','*','*'] for i in range(3)]

print("""The game has started
Input two numbers in range 1 to 3
The first signifies row second signifies column""")


valid_inputs = ['1', '2', '3']
for i in range(3):
    for j in range(3):
        print(board[i][j],end =' ')
    print('')
while True:
    move = None
    while move == None:
        move = input("\nMake your move : ").strip()
        if move[0] not in valid_inputs or move[-1] not in valid_inputs:
            print("\nInvalid input")
            move = None
        row = int(move[0])-1
        column = int(move[-1])-1
        if board[row][column]!='*':
            print("\nInvalid input")
            move = None
    board[row][column] = 'x'

    for i in range(3):
        for j in range(3):
            print(board[i][j],end =' ')
        print('')

    c.send(bytes(move,'utf-8'))

    msg = c.recv(12).decode()
    if(msg == 'W'):
        print("\n\nYou won!")
        break

    elif(msg == 'T'):
        print("\n\nMatch ended up in a tie")
        break

    else:
        print("\nBot moved : {} {}".format(msg[1],msg[2]))    
        board[int(msg[1])-1][int(msg[2])-1] = 'o'
        for i in range(3):
            for j in range(3):
                print(board[i][j],end =' ')
            print('')
        if(msg[0]=='L'):
            print("\n\nYou lost")
            break
