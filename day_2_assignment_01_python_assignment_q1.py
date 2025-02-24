# -*- coding: utf-8 -*-
"""DAY  2 : ASSIGNMENT 01-PYTHON ASSIGNMENT   Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AJSdZ3KJm6ODlvfNS71X-fj-KPH2QJ4A

DAY  2 : ASSIGNMENT 01-PYTHON ASSIGNMENT  
Q1
"""

#A) WAP to add 50 and 60 to L.
L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)

#B) WAP to remove 11 and 13from L.
L = [11, 12, 13, 14]
L.remove(11)
L.remove(13)
print(L)

#C) WAP to sort L in ascending order
L = [11, 12, 13, 14]
L.sort()
print(L)

#D) WAP to sort L in descending order.
L = [11, 12, 13, 14]
L.sort(reverse=True)
print(L)

#E) WAP to search for 13 in L.
L = [11, 12, 13, 14]
if 13 in L:
    print("13 is present in L")
else:
    print("13 is not present in L")

#F) WAP to count the number of elements present in L.
L = [11, 12, 13, 14]
count = len(L)
print("Number of elements in L:", count)

#G) WAP to sum all the elements in L.
L = [11, 12, 13, 14]
sum_elements = sum(L)
print("Sum of all elements in L:", sum_elements)

#H) WAP to sum all ODD numbers in L.
L = [11, 12, 13, 14]
sum_odd = sum(num for num in L if num % 2 != 0)
print("Sum of all odd numbers in L:", sum_odd)

#I) WAP to sum all EVEN numbers in L.
L = [11, 12, 13, 14]
sum_even = sum(num for num in L if num % 2 == 0)
print("Sum of all even numbers in L:", sum_even)

#J) WAP to sum all PRIME numbers in L.
def is_prime(n):
    if n <= 1:
      return False
    if n == 2:
        return True
L = [11, 12, 13, 20]
sum_prime = sum(num for num in L if is_prime(num))
print("Sum of all prime numbers in L:", sum_prime)

#K) WAP to clear all the elements in L.

L = [11, 12, 13, 14]
L.clear()
print("L after clearing all elements:", L)

#L) WAP to delete L.
L = [11, 12, 13, 14]
del L
print("L is deleted")

"""Q2  D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.
  
"""

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

#(i)	WAP to add new entry in D; key=8 and value is 8.8
D[8] = 8.8
print("Dictionary after adding new entry:", D)

#(ii)	WAP to remove key=2.
if 2 in D:
  del D[2]
  print("Dictionary after removing key=2:", D)
else:
  print("Key=2 is not present in the dictionary.")

#(iii)	WAP to check weather 6 key is present in D.
if 6 in D:
    print("Key=6 is present in the dictionary.")
else:
    print("Key=6 is not present in the dictionary.")

#(iv)	WAP to count the number of elements present in D.
num_elements = len(D)
print("Number of elements in the dictionary D:", num_elements)

#(v)	WAP to add all the values present D.
total_sum = sum(D.values())
print("Sum of all values in the dictionary D:", total_sum)

#(vi)	WAP to update the value of 3 to 7.1.
if 3 in D:
       D[3] = 7.1
       print("Dictionary after updating key=3:", D)
else:
    print("Key=3 is not present in the dictionary.")

#(vii)	WAP to clear the dictionary Code :
D.clear()
print("Dictionary D after clearing all elements:", D)

""" Q3.S1 is a set defined as S1= [10, 20, 30, 40, 50, 60].

 S2 is a set defined as S2= [40, 50, 60, 70, 80, 90]   

"""

S1= [10, 20, 30, 40, 50, 60]
S2= [40, 50, 60, 70, 80, 90]

#A)WAP to add 55 and 66 in Set S1.
S1 = {10, 20, 30, 40, 50, 60}
S1.add(55)
S1.add(66)
print("Set S1 after adding 55 and 66:", S1)

#C) WAP to remove 10 and 30 from Set S1.
S1 = {10, 20, 30, 40, 50, 60}
# Removing elements from the set
S1.discard(10)
S1.discard(30)
print("Set S1 after removing 10 and 30:", S1)

#D) WAP to check whether 40 is present in S1.

S1 = {10, 20, 30, 40, 50, 60} # Checking if an element is present if 40 in S1:     print("40 is present in S1") else:
print("40 is not present in S1")

#E)  WAP to find the union between S1 and S2
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)

#F)  WAP to find the intersection between S1 and S2.

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)

#G) WAP to find the S1 - S2.

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
difference_set = S1 - S2
print("Set difference (S1 - S2):", difference_set)

"""Q4
Write the following program.  
(i)	WAP to print 100 random strings whose length between 6 and 8.  
(ii)	WAP to print all prime numbers between 600 and 800.  
(iii)	WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.

"""

#(i) WAP to print 100 random strings whose length between 6 and 8.
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def main():
    random_strings = [generate_random_string(random.randint(6, 8)) for _ in range(100)]
    for index, s in enumerate(random_strings, start=1):
        print(f"{index:03d}: {s}")

if __name__ == "__main__":
    main()

#(ii) WAP to print all prime numbers between 600 and 800.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    primes = [num for num in range(600, 801) if is_prime(num)]
    for prime in primes:
        print(prime)

if __name__ == "__main__":
    main()

#(iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.
def main():
    for num in range(100, 1001):
        if num % 7 == 0 and num % 9 == 0:
            print(num)

if __name__ == "__main__":
    main()

"""DAY 2 : ASSIGNMENT 01-PYTHON ASSIGNMENT

Q5. WAP to create two lists of 10 random numbers between 10 and 30; Find  
(i)	Common numbers in the two lists

(ii)	Unique numbers in both the list

(iii)	Minimum in both the list

(iv) 	Maximum in both the list  Sum of both the lists  

"""

import random

# Generate two lists of 10 random numbers between 10 and 30
list1 = [random.randint(10, 30) for _ in range(10)]
list2 = [random.randint(10, 30) for _ in range(10)]

# (i) Common numbers in the two lists
common_numbers = list(set(list1) & set(list2))

# (ii) Unique numbers in both lists
unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))

# (iii) Minimum in both lists
min_list1 = min(list1)
min_list2 = min(list2)

# (iv) Maximum in both lists
max_list1 = max(list1)
max_list2 = max(list2)

# Sum of both lists
sum_list1 = sum(list1)
sum_list2 = sum(list2)
total_sum = sum_list1 + sum_list2

# Print results
print("List 1:", list1)
print("List 2:", list2)
print("Common numbers:", common_numbers)
print("Unique numbers in List 1:", unique_list1)
print("Unique numbers in List 2:", unique_list2)
print("Minimum in List 1:", min_list1)
print("Minimum in List 2:", min_list2)
print("Maximum in List 1:", max_list1)
print("Maximum in List 2:", max_list2)
print("Sum of List 1:", sum_list1)
print("Sum of List 2:", sum_list2)
print("Total sum of both lists:", total_sum)

"""Q6. WAP to create a list of 100 random numbers between 100 and 900. Count and print the:  
(i)All odd numbers

(ii)All even numbers

(iii)All prime numbers

"""

import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Generate a list of 100 random numbers between 100 and 900
    random_numbers = [random.randint(100, 900) for _ in range(100)]

    # Find all odd numbers
    odd_numbers = [num for num in random_numbers if num % 2 != 0]

    # Find all even numbers
    even_numbers = [num for num in random_numbers if num % 2 == 0]

    # Find all prime numbers
    prime_numbers = [num for num in random_numbers if is_prime(num)]

    # Print results
    print("Random Numbers:", random_numbers)
    print("Count of odd numbers:", len(odd_numbers))
    print("Odd numbers:", odd_numbers)
    print("Count of even numbers:", len(even_numbers))
    print("Even numbers:", even_numbers)
    print("Count of prime numbers:", len(prime_numbers))
    print("Prime numbers:", prime_numbers)

if __name__ == "__main__":
    main()

"""Q7. D is a dictionary defined as D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}. WAP to read all the keys and values from dictionary and write to the file in the given below format. Key1, Value1 Key2, Value2 Key3, Value3  """

D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
with open("output.txt", "w") as file:
    for key, value in D.items():
        file.write(f"Key{key}, Value{value}\n")
print("Dictionary has been written to output.txt")

"""Q8. L is a list defined as L={"One","Two","Three","Four","Five"}. WAP to count the length of reach element from a list and write to the file in the given below format: One, 3 Two, 3 Four, 4"""

L = ["One", "Two", "Three", "Four", "Five"]
file_name = "lengths.txt"

with open(file_name, 'w') as file:
    for item in L:
        length = len(item)
        file.write(f"{item}, {length}\n")

print(f"Element lengths have been written to '{file_name}'.")

"""Q8.Write to the file 100 random strings whose length between 10 and 15.  """

import random
import string

file_name = "random_strings.txt"
def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))
with open(file_name, 'w') as file:
    for _ in range(100):
        length = random.randint(10, 15)
        random_string = generate_random_string(length)
        file.write(random_string + '\n')
print(f"100 random strings have been written to '{file_name}'.")

"""Q10. Write to the file all prime numbers between 600 and 800.  """

file_name = "prime_numbers.txt"

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Open the file in write mode
with open(file_name, 'w') as file:
    # Iterate through the range 600 to 800
    for num in range(600, 801):
        if is_prime(num):
            file.write(f"{num}\n")

print(f"Prime numbers between 600 and 800 have been written to '{file_name}'.")

"""Q11. WAP to calculate the time taken by a program."""

import time
start_time = time.time()
sum_result = sum(range(1, 1000001))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken by the program: {elapsed_time:.6f} seconds")

""" Q12. WAP to sort following number of elements in a list, calculate time taken and plot the graph. Number of elements in list Time Taken 5k T1 10k T2 15k T3 20k T4 25k T5  """

import time
import matplotlib.pyplot as plt

# Function to sort and measure time
def sort_and_measure_time(n):
    # Create a list of n elements with random integers
    random_list = list(range(n))
    random.shuffle(random_list)  # Shuffle the list to make it random

    # Measure the time taken to sort the list
    start_time = time.time()
    sorted_list = sorted(random_list)
    end_time = time.time()

    return end_time - start_time

# Number of elements in each list
elements = [5000, 10000, 15000, 20000, 25000]

# Measure time taken for each list size
times_taken = []
for n in elements:
    time_taken = sort_and_measure_time(n)
    times_taken.append(time_taken)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(elements, times_taken, marker='o', linestyle='-', color='b', label='Time Taken')
plt.title('Time Taken to Sort Lists of Different Sizes')
plt.xlabel('Number of Elements in List')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

"""Q13. WAP to create a dictionary of student marks in five subjects and you have to  find the student having maximum and minimum average marks"""

# Dictionary of student marks
student_marks = {
    'Alice': [85, 90, 92, 88, 89],
    'Bob': [79, 82, 85, 78, 80],
    'Charlie': [90, 92, 88, 85, 86],
    'David': [72, 68, 74, 75, 70],
    'Eve': [95, 98, 96, 97, 94]
}

average_marks = {}
for student, marks in student_marks.items():
    average_marks[student] = sum(marks) / len(marks)
max_student = max(average_marks, key=average_marks.get)
min_student = min(average_marks, key=average_marks.get)

# Print results
print("Student marks:")
for student, marks in student_marks.items():
    print(f"{student}: {marks}")

print("\nAverage marks:")
for student, avg in average_marks.items():
    print(f"{student}: {avg:.2f}")

print(f"\nStudent with maximum average marks: {max_student} ({average_marks[max_student]:.2f})")
print(f"Student with minimum average marks: {min_student} ({average_marks[min_student]:.2f})")