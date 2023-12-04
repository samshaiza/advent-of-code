import re

with open("input.txt", "r") as f:
    text = f.readlines()

ans = 0
ans2 = 0

for l in text:

    matched_nums = 0
    points = 0

    game_num = re.findall('\d+', l.split(":")[0])[0]
    winning_nums = l.split(":")[1].split("|")[0].strip().split()
    nums_given = l.split(":")[1].split("|")[1].strip().split()
    for i in winning_nums:
        
        if (i in nums_given) and points == 0:
            points = points + 1
            matched_nums += 1
        if (i in nums_given) and points >= 1:
            points = points * 2
            matched_nums += 1
    
    print(game_num)
    print(nums_given) 
    ans += points/2

print(ans)
