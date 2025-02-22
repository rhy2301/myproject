import random

num_players = 4
players_list = input("참가자를 입력하시오: ").split()
height = 5

ladder = [["|" if col % 2 == 0 else " " for col in range(num_players*2-1)]for _ in range(height)]

for row in range(height):
    for col in range(1, num_players*2-2, 2):
        if random.random() < 0.6:
            if col > 1 and ladder[row][col-2] == "-":
                continue

            ladder[row][col] = "-"
            
            if ladder[row][col + 1] != "|":
                ladder[row][col + 1] = " "
            
for row in ladder:
    print("".join(row))

for i, player in enumerate(players_list):
    
    row, col = 0, 2*i
    
    while row <= len(ladder)-1:
        if col > 0 and ladder[row][col-1] == "-":
            col -= 2
            
        elif col < len(ladder[col])-1 and ladder[row][col+1] == "-":
            col += 2
            
        row += 1
    
    result = col // 2
    print(player, result)