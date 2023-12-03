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
           
            if (color == "green"):
                green = max(int(num), green)
            elif (color == "red"):
                red = max(int(num), red)
            elif (color == "blue"):
                blue = max(int(num), blue)
    if good_game:
        
        ans2 += (green * red * blue)
        print("green: " + str(green) + ", red: " + str(red) + ", blue: " + str(blue) + " = " + str(ans2))
        ans += int(game.split()[-1])
        

print(ans2)
