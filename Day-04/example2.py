import random

# 🚨 Don't change the code below 👇

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)

id_random = random.randint(0,num_items - 1)
print(names[id_random])