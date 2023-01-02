print('----------WLCOME TO TREASURE GAME------------')

row = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
matrix = [row, row1, row2]
print(f'{row}\n{row1}\n{row2}')


position = input('Where do you want to put the treasure???\n')
vertical = int(position[1])
harizantal = int(position[0])
selected_row_culmn = matrix[vertical - 1][harizantal - 1] = 'X'
print(f'{row}\n{row1}\n{row2}')
