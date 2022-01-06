# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_as_lower = name1.lower()
name2_as_lower = name2.lower()

score_true = 0
score_love = 0

if name1_as_lower.count("t") > 0 or name2_as_lower.count("t") > 0: 
    score_true = score_true + name1_as_lower.count("t") + name2_as_lower.count("t")
    
if name1_as_lower.count("r") > 0 or name2_as_lower.count("r") > 0: 
    score_true = score_true + name1_as_lower.count("r") + name2_as_lower.count("r")
    
if name1_as_lower.count("u") > 0 or name2_as_lower.count("u") > 0: 
    score_true = score_true + name1_as_lower.count("u") + name2_as_lower.count("u")
    
if name1_as_lower.count("e") > 0 or name2_as_lower.count("e") > 0: 
    score_true = score_true + name1_as_lower.count("e") + name2_as_lower.count("e")



if name1_as_lower.count("l") > 0 or name2_as_lower.count("l") > 0: 
    score_love = score_love + name1_as_lower.count("l") + name2_as_lower.count("l")
    
if name1_as_lower.count("o") > 0 or name2_as_lower.count("o") > 0: 
    score_love = score_love + name1_as_lower.count("o") + name2_as_lower.count("o")
    
if name1_as_lower.count("v") > 0 or name2_as_lower.count("v") > 0: 
    score_love = score_love + name1_as_lower.count("v") + name2_as_lower.count("v")
    
if name1_as_lower.count("e") > 0 or name2_as_lower.count("e") > 0: 
    score_love = score_love + name1_as_lower.count("e") + name2_as_lower.count("e")


score_total = str(score_true) + str(score_love)
score_total_int = int(score_total)

if score_total_int < 10 or score_total_int > 90:
    print(f'Your score is {score_total_int}, you go together like coke and mentos.')
    
elif score_total_int >= 40 and score_total_int <= 50:
    print(f'Your score is {score_total_int}, you are alright together.')

else:
    print(f'Your score is {score_total_int}.')





    
