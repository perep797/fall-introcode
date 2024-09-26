from unit1lesson2 import *

#Question 1: Smallest number
number_list.sort()
print("The smallest number is:", number_list[0])

#Question 2: Closest number to 500
def closest(number_list, K):
     
    return number_list[min(range(len(number_list)), key = lambda i: abs(number_list[i]-K))]
     
K = 500
print("The closest number to 500 is:", closest(number_list, K))

#Question 3: Smallest even number
even_numbers = []
for num in number_list:
    if num % 2 == 0:
        even_numbers.append(num)
        even_numbers.sort()
print("The smallest even number is:", even_numbers[0])
        
#Question 4: Last word alphabetically 
word_list.sort(reverse = True)
print("The last word alphabetically is:", word_list[0])

#Question 5: The longest word
word = max(word_list, key = len)
print("The longest word is: " + word)

