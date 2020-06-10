user_input = list(input("Enter names seperated by comma :").title().split(","))

with open("people.txt", "r")as my_file:
    files = my_file.read().splitlines() #it will remove \n quote

new_list= [ ]
for file in files:
    new_list.append(file)
# this will find intersection
intersection_set = set.intersection(set(user_input),set(new_list))
intersection_list = list(intersection_set)
print(intersection_list)

with open("nearby_friends.txt", "w") as my:
    my.writelines(["%s\n" % item  for item in intersection_list])

