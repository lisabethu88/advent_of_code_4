f = open("input", "r")

pairs = 0
line_list = []
for line in f:
    line = line.strip()
    line_list.append(line)
    new_list = line.split(",")
    first_pair = new_list[0]
    first_pair = first_pair.split("-")
    second_pair = new_list[1]
    second_pair = second_pair.split("-")
    if int(first_pair[0]) == int(second_pair[0]):
        pairs += 1
    elif int(first_pair[1]) == int(second_pair[1]):
        pairs += 1
    elif int(first_pair[0]) > int(second_pair[0]):
        if int(first_pair[0]) <= int(second_pair[1]):
            pairs += 1
    elif int(second_pair[0]) > int(first_pair[0]):
        if int(second_pair[0]) <= int(first_pair[1]):
            pairs += 1
f.close()
print(pairs)
#3
#5
