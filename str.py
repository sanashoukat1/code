import random

name_string = input("Give me everybody's names, seperated by a comma.")
name = name_string.split(", ")

num_items = len(name)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = random.choice(name)
print(person_who_will_pay + " is going to buy the meal today.")