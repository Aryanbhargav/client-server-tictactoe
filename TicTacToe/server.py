import socket
import random
class TicTacToe():
    def __init__(self):
        self.board = [['*','*','*'] for i in range(3)]
        self.empty = []
        for i in range(3):
            for j in range(3):
                self.empty.append((i,j))
    def move(self):
        r,c = random.choice(self.empty)
        self.empty.remove((r,c))
        self.board[r][c] = 'o'
        return (r+1,c+1)

    def eval(self):
        for row in range(3) :
            if (self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]) :
                if (self.board[row][0] == 'x') :
                    return 1
                elif (self.board[row][0] == 'o') :
                    return -1

        for col in range(3) :
            if (self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]) :
                if (self.board[0][col] == 'x') :
                    return 1
                elif (self.board[0][col] == 'o') :
                    return -1

        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) :
            if (self.board[0][0] == 'x') :
                return 1
            elif (self.board[0][0] == 'o') :
                return -1

        if (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]) :
            if (self.board[0][2] == 'x') :
                return 1
            elif (self.board[0][2] == 'o') :
                return -1

        return 0

    def isOver(self):
        return (len(self.empty)==0)


s=socket.socket()
host='localhost'
port = 9991
s.bind((host, port))
s.listen(2)

print('socket is listening')
while True:
    client,add = s.accept()

    game = TicTacToe()
    print("\nA client has started the game\n")
    while True:
        clientMove = client.recv(512).decode()
        cr = int(clientMove[0])-1
        cc = int(clientMove[-1])-1

        print("\nClient moved : {} {}".format(cr,cc))

        game.board[cr][cc]='x'
        game.empty.remove((cr,cc))
        for i in range(3):
            for j in range(3):
                print(game.board[i][j],end=' ')
            print('')
        gameState = game.eval()
        if(gameState == 1):
            client.send(bytes('W','utf-8'))
            print("\n\nClient won")
            client.close()
            break
        elif(gameState == 0):
            if(game.isOver()):
                client.send(bytes('T','utf-8'))
                print('\n\nMatch ended up in a tie')
                client.close()
                break
        r,c = game.move()
        print("\nServer moved : {} {}".format(r,c))
        for i in range(3):
            for j in range(3):
                print(game.board[i][j],end=' ')
            print('')
        gameState = game.eval()

        if gameState == -1:
            client.send(bytes('L' + str(r) + str(c),'utf-8'))
            print("\n\nServer won")
            client.close()
            break
        else:
            client.send(bytes('O' + str(r) + str(c),'utf-8'))




        

