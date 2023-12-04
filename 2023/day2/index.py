import re

with open("input.txt", "r") as f:
    txt = f.readlines()
ans = 0
ans2 = 0
for line in txt:
    good_game = True
    green = 0
    red = 0
    blue = 0
    game, line = line.split(":")
    res = 0
    for e in line.split(";"):
        for b in e.split(','):
            num, color = b.split()
            if int(num) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                good_game = False
            if (color == "green"):
                green += int(num)
            elif (color == "red"):
                red += int(num)
            elif (color == "blue"):
                blue += int(num)
    if good_game:
        
        ans2 += (green * red * blue)
        print("green: " + str(green) + ", red: " + str(red) + ", blue: " + str(blue) + " = " + str(ans2))
        ans += int(game.split()[-1])
        

print(ans2)
