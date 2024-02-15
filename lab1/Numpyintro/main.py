import numpy as np
import checkers as check

def main():
  size = game()
  board = check.generate_board(size)
  check.get_count(board)

def game():
    size = int(input('What size board do you want to play? '))
    return size

if __name__ == '__main__':
    main()

