#Lesson3
#1. Create a list containing five different fruits and print the third fruit.
fruits = ['Apple','Banana','Grape', 'Peach', 'Chery']
print(fruits[2])

#2. Create two lists of numbers and concatenate them into a single list.
odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]
numbers = odd_numbers + even_numbers
print(numbers)

#3. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1,2,3,4,5,6,7,8,9,75,48,6,3,2,1,4]
new_numbers = [numbers[0], numbers [len(numbers)//2], numbers[-1]]
print(new_numbers)

#4. Create a list of your five favorite movies and convert it into a tuple.
favourite_movie = ['Gladiator', 'Real steel', 'Tarzan', 'Nokdaun', 'War Horse']
favourite_movie1 = tuple(favourite_movie)
print(favourite_movie1)

#5. Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['London','New York','Berlin','Samarkand','Lisabon','Paris']
if 'Paris' in cities: 
    print ('Yes, Paris is in this list')
else:
    print('No, Paris is not in this list.')

#6. Create a list of numbers and duplicate it without using loops.
l1 = [1,2,23,4,56,98,436]
l2 = l1.copy()
print(l2)

#7. Given a list of numbers, swap the first and last elements.
numbers7 = [1,2,23,45,67,87,78,79,97,100]
#swap the first and last elements 
numbers7 [0], numbers7 [-1] = numbers7 [-1], numbers7 [0]
print(numbers7)

#8. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers8 = tuple(range(1,11))

#Slice from index 3 to 7 
sliced = numbers8[3:7]

print(sliced)

#9. Create a list of colors and count how many times "blue" 
#appears in the list.
colours = ['Blue', 'Red', 'Yellow', 'Blue', 'Black', 'Purple', 'Pink', 'Blue']

#Count how many times does blue appeares
count = colours.count('Blue')

print('Blue appears', count, 'times')

#10 Given a tuple of animals, find the index of "lion".
animals = ('Lion', 'Horse', 'Tiger', 'Giraffe', 'Cow', 'Dog')
lions_index = animals.index('Lion')
print("Lion's index is", lions_index)


#11. Create two tuples of numbers and merge them into a single tuple.
num1 = (1,2,2,3,4,4,5,56,7,67,8,10)

num2 = (3,5,6,7,8,9,2,4,5,78,95)

merged_num = num1 + num2

print('Merged numbers list :', merged_num)


#12. Given a list and a tuple, find and print their lengths.
# Define list and tuple
my_list = ['a', 'b', 'c', 1,2,3,4,[1,2,3]]

my_tuple = (19,28,37,46,59,'y','x')

# Find and define their length
print('Length of list is :', len(my_list))
print('Lenth of tuple is :', len(my_tuple))

#13. Create a tuple of five numbers and convert it into a list.
# Define tuple of numbers
t_numbers = (1,2,3,4,5)

# Convert tuple of numbers into list
l_numbers = list(t_numbers)

print(l_numbers)

#14. Given a tuple of numbers, find and print the maximum and minimum values.
numbers14 = (1,2,3,4,5)

maximum = max(numbers14)

minimum = min(numbers14)

print('Maximum value is :', maximum)
print('minimum value is :', minimum)


#15 Create a tuple of words and print it in reverse order.
cars = ('BMW', 'Mercedes', 'Porsche', 'Mustang', 'Lamborgini', 'Ferrari', 'Ford')

r_tuple = tuple(reversed(cars))

print('Tuple of super cars is :', r_tuple)










