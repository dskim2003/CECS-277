'''
The 'in' keyword allows you to create a boolean expression 
based on whether an equal object is in a given list.
'''
my_list = ['Apples', 'Bananas', 'Cherries']

if 'Apples' in my_list:
    print('I found Apples!')
if 'Bananas' in my_list:
    print('I found Bananas!')
if 'Carrots' in my_list:
    print("I found Carrots!")
if 'Oranges' not in my_list:
    print("I didn't find Oranges!")

'''
Output:
I found apples!
I found bananas!
I didn't find Oranges!
'''



'''
The 'in' keyword also works for strings!
Note that lowercase and uppercase are considered different characters.
'''
my_word = 'The Alphabet'

if 'h' in my_word:
    print('I found the character "h"!')
if 'H' in my_word:
    print('I found the character "H"!')

'''
Output:
I found the character "h"!
'''



'''
(This is optional!!!)
Want to do something fancy?
You can use list comprehension to quickly process lists!
'''
sentence = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
vowels = 'AEIOU'

consonants = [letter for letter in sentence if letter not in vowels]
'''
We iterate through the list 'sentence'.
For each element we evaluate, we assign it the name 'letter' to use in the condition after the if.
If 'letter' makes the if clause true, it is appended to the list, in the order we iterated through it.
So, 'consonants' contains all elements of 'sentence' that is not in 'vowels'.
'''
# we constructed consonants as a list, so we have to cast it back to a string to print it properly
print(''.join(consonants))

'''
Output:
TH QCK BRWN FX JMPS VR TH LZY DG
'''

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [number for number in my_numbers if number%2 == 0]
print(evens)
'''
Output:
[2, 4, 6, 8, 10]
'''

tripled_numbers = [number*3 for number in my_numbers]
print(tripled_numbers)
'''
Output:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
'''