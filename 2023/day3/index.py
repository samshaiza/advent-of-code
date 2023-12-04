list = []

# holds numbers
number_list = []

# holds symbols
symbols = []

# holds symbol loacations
symbol_locations = []

# holds locations of gears
gear_locations = []

# open file
with open("input.txt", "r") as f:
    for t in f:
        line = t.strip()
        list.append(line)

# add all the symbols and their locations
length = len(list[0])
for y, i in enumerate(list):
    for x, j in enumerate(i):
        if j != "." and not(j.isdigit()):
            symbols.append(j) 
            symbol_locations.append((x, y))
            if j == "*":
                gear_locations.append((x, y))
    
# used to find the start and end to a file
active_number = False

for y, l in enumerate(list):
    for x, c in enumerate(l):
        if not(active_number) and (c == "." or c in symbols):
            continue 
        elif not(active_number) and c.isdigit():
            curr_num = c
            active_number = True 
            x1 = x
        elif active_number and (c == "." or c in symbols):
            new_num = int(curr_num)
            x2 = x - 1
            number_list.append((new_num, x1, x2, y))
            active_number = False
            curr_num = ""
        elif active_number and c.isdigit():
            curr_num += c
            if x == length - 1:
                new_num = int(curr_num)
                x2 = x - 1
                number_list.append((new_num, x1, x2, y))
                active_number = False
                curr_num = ""

ans = 0

for number, x, x2, y in number_list:
    border_p = []
    for why in range(y-1, y+2):
        for ex in range(x-1, x2+2):
            border_p.append((ex, why))

    intersect_list = set(symbol_locations) & set(border_p)
    if (len(intersect_list) > 0):
        ans += number
    # print("border points: " + str(border_p))

ans2 = 0

for x, y in gear_locations:
    border_gears = []
    gear_nums = []
    for dy in range(y-1, y+2):
        for dx in range(x-1, x+2):
            border_gears.append((dx, dy))
    for number, x, x2, y in number_list:        
        if (x, y) in border_gears or (x2, y) in border_gears:
            gear_nums.append(number)
    if len(gear_nums) == 2:
        n1, n2 = gear_nums
        ans2 += n1 * n2
    print(border_gears)

print(ans2)

