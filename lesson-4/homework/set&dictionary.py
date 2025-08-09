# Lesson - 4
#1. Write a Python script to sort (ascending and descending) a dictionary by value.
sort_dic = {'FirstName' : 'Jack', 'Lastname': 'Grealish', 'Country': 'England'}

# Ascending by value
for key, value in sorted(sort_dic.items(), key=lambda item: item[1]):
    print(f"{key}: {value}")

print()

# Descending by value
for key, value in sorted(sort_dic.items(), key=lambda item: item[1], reverse=True):
    print(f"{key}: {value}")

# 2.Write a Python script to add a key to a dictionary.
second_dic = {0: 10, 1: 20}

second_dic[2] = 30

print(second_dic)

#3. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}

dic2 = {3: 30, 4: 40}

dic3 = {5: 50, 6: 60}

# I have used unpucking here 
new_dic = {**dic1, **dic2, **dic3}

print(new_dic)

#4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5

dict4 = {x: x*x for x in range(1, n + 1)}

print(dict4)

# 5. Write a Python script to print a dictionary where the keys are numbers between 
# 1 and 15 (both included) and the values are the square of the keys.
dict5 = {x: x*x for x in range(1, 16)}

# print dictionary
print(dict5)


## Set exercises

# 1. Write a Python program to create a set.
set1 = {50, 20, 70, 60, 10, 40, 20}

print(set1)

# 2. Write a Python program to iterate over sets.
set2 = {'Banana', 'Apple', 'Cherry', 'Pineapple', 'Grape'}

for item in set2:
    print(item)

# 3. Write a Python program to add member(s) to a set.
subjects = {'History', 'Math', 'English', 'Economics', 'Physics', 'Russian' }

subjects.add('Chemistry')

print(subjects)

# 4. Write a Python program to remove item(s) from a given set.
top_players = {'Ronaldo: CR7', 'Messi', 'Neymar', 'Levandovskiy', 'Marcello', 'Zidane', 'Darvin Nunes'}

top_players.remove('Darvin Nunes')

print(top_players)

# 5. Write a Python program to remove an item from a set if it 
# is present in the set.
uzbek_dishes = {'Palov', 'Somsa', 'Manti', 'Chuchvara', 'Kuk Somsa', 'Sushi'}

if 'Sushi' in uzbek_dishes:
    uzbek_dishes.remove('Sushi')
    print(f'Updated set: {uzbek_dishes}')
