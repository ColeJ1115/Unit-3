from numpy import array
from numpy import random
from numpy import zeros

def generate_board(size):
    pieces = ['Red', 'Black', 'Empty']
    board = random.choice(pieces, size = (size,size))
    print(board)
    return board

def get_count(board):
    red_count = (board == 'Red')
    print(f'The sum of red is {red_count.sum()}')
    black_count = (board == 'Black')
    print(f'The sum of black is {black_count.sum()}')
    empty_count = (board == 'Empty')
    print(f'The sum of empty spaces are {empty_count.sum()}')

if __name__ == '__main__':
    print('This is not the main file')