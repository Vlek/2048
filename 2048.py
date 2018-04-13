from random import randint

class twoohfoureight:    
    def __init__(self):
        #Init the board and apply pieces:
        self.board = self.boardInit()
        self.addRandomPiece(2, True)
        self.score = 0

    def boardInit(self):
        return [ [ ' ' for i in range(4) ] for i in range(4) ]

    def addRandomPiece(self, n, twosOnly=False):
        '''adds random piece n times'''
        for addition in range(n):
            #taking advantage of list referencing to add a piece.
            rowPool = [i for i in self.board if ' ' in i]
            inter = rowPool[randint(0, len(rowPool)-1)]
            step = randint(0, inter.count(' ') - 1)
            index = 0
            while step > 0:
                index = inter.index(' ', index)
                step -= 1
            if twosOnly:
                inter[index] = 2
            else:
                inter[index] = (2 if randint(0, 3) <= 2 else 4)

    def printBoard(self):
        for i in self.board:
            print('|\t{}\t|\t{}\t|\t{}\t|\t{}\t|'.format(i[0],i[1],i[2],i[3]))

    def move(self, direction):
        '''modifies the board orientation, then takes care of the move based
        on the 'right' movement, then orients the board back'''
        if direction in ['up', 'down', 'left', 'right']:

            #Reorient the board so that there only needs to be one move function
            directions = {'up':(3,1),'down':(1,3),'left':(2,2)}
            if direction in ['up','down','left']:
                self.boardOrientation(directions[direction][0])
            result = []
            oldBoard = list(self.board)

            #Perform the move
            for i in self.board:
                
                #If it's not blank, then proceed to move pieces
                if i != [' ',' ',' ',' ']:
                    
                    intermediary = list(i)

                    #Remove blank spaces
                    while intermediary.count(' ') > 0:
                        intermediary.pop(intermediary.index(' '))

                    #If there's more than one piece, see if they need to merge
                    if len(intermediary) > 1:
                        i = 1
                        while i < len(intermediary):
                            if intermediary[-i] == intermediary[-i - 1]:
                                intermediary[-i] *= 2
                                self.score += intermediary[-i]
                                intermediary.pop(-i - 1)
                            i += 1
                    addBlanks = [' '] * (4 - len(intermediary))
                    addBlanks.extend(intermediary)
                    i =  addBlanks

                #Regardless of what happens, make sure that the row appears in the board again
                result.append(i)
            self.board = result

            #Check whether the board even changed, and add a piece if it did.
            if result == oldBoard:
                raise NameError("Unacceptable Move: Does not change board")
            else:
                self.addRandomPiece(1)

            #Put the board back the way that it was
            if direction in ['up','down','left']:
                self.boardOrientation(directions[direction][1])

        #Sorry, didn't understand the move
        else:
            raise NameError("Unacceptable Move: not a direction")
        self.printBoard() #this is a placeholder

    def boardOrientation(self, reorientTimes):
        '''reorients the board so that the right movement is able to take care of all movement directions.
        Should be used once to put the board so that the right action performs the move,
        then put back to display the board as it should be'''
        for i in range(reorientTimes):
            result = []
            microResult = []
            for column in range(4):
                for row in range(4):
                    microResult.append(self.board[row][column])
                result.append(microResult)
                microResult = []
            self.board = [result[i] for i in reversed(range(4))]

if __name__ == '__main__':
    game = twoohfoureight()
    game.printBoard()
