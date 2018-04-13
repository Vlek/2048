#!/usr/bin/env python3

from random import choice, randint

class Twoohfoureight:
    def __init__(self):
        self.map = [[0]*4 for i in range(4)]
        self._add_random_piece(2)

    def print_map(self):
        for i in self.map:
            #print('\t'.join(map(str, i)))
            print(i)

    def _add_random_piece(self, num_pieces=1):
        for i in range(num_pieces):
            available_slots = []
            for row in range(4):
                for column in range(4):
                    if self.map[row][column] == 0:
                        available_slots.append([row, column])
            # TODO: Check len of available_slots for a spot.
            # if one is not available, then game over.
            chosen = choice(available_slots)
            self.map[chosen[0]][chosen[1]] = (4 if randint(1, 10) == 1 else 2)

    def _rotate(self, rotations=1):
        for rotation in range(rotations):
            result = [[] for i in range(4)]
            for r in range(3, -1, -1):
                for c in range(4):
                    result[c].append(self.map[r][c])
            self.map = result
            
    def move(self, direction=0):
        """
        This is my favorite part of making the game. I use this list of lists
        in order to decide how many times I rotate the game board in order
        to do a standard left-to-right move so that the algorithm is super simple
        """
        moves = [
            [3, 1],
            [2, 2],
            [1, 3],
            [0, 0]
        ]

        self._rotate(moves[direction][0])

        for row in range(4):
            r = [i for i in self.map[row] if i != 0]

            r_result = []
            while(len(r)):
                num = r.pop(0)
                if len(r) and num == r[0]:
                    num += r.pop(0)
                    # TODO: Do a 2048 check here to see if the player won?
                    # this might not be the best place because we could use
                    # this method to run tests to see if the player has any valid moves
                r_result.append(num)
                    
            self.map[row] = r_result + [0]*(4-len(r_result))

        self._add_random_piece()

        self._rotate(moves[direction][1])
        self.print_map()

g = Twoohfoureight()
g.print_map()
