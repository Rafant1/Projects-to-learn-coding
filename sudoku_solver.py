

board = [
    ['-',1,'-',6,'-',4,3,'-',7],
    [3,5,6,'-','-','-','-','-','-'],
    ['-','-','-','-',5,3,6,9,'-'],
    ['-',8,3,2,6,'-',4,'-',9],
    ['-','-','-','-','-','-','-','-','-'],
    [4,'-',5,'-',7,8,2,6,'-'],
    ['-',4,2,5,3,'-','-','-','-'],
    ['-','-','-','-','-','-',7,2,4],
    [7,'-',9,4,'-',2,'-',8,'-']
]

def print_board(board):
    position2 = 0
    for column in board:
        position = 0
        if position2 == 27 or position2 == 54:
            print('---------------------')

        for element in column:
            position += 1
            position2 += 1
            if position % 9 != 0 and position / 3 != 1 and position / 3 != 2:
                print(element, end=' ')


            elif position % 9 == 0:
                print(element, end='\n')



            elif position / 3 == 1 or position /3 == 2:
                print(f"{element} | ", end='')










print_board(board)



