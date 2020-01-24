#!/usr/bin/env python3

## This is the first problem set.  You task is to create and compute various variables
## and do other tricks in the code.
## Always provide suitable output by printing your results
## so that people who are familiar with the problem understand what is going on.
## 'People familiar...' include your graders and instructors and classmates,
## you do not have to cater for a random person from street
## (less context printing required if you use notebooks)

## You probably notice that these tasks are somewhat similar to your first problem sets in
## info 201.  However, now we ask you to perform these in python.

## -------------------- Defining variables --------------------
## Here we ask you to define, compute, and print a number of variables
## ---------- Example: ----------
## Create variable `my_name` that is equal to your first name
my_name = "Ott"
print("I am", my_name)
## ---------- end of the example ----------


## -------------------- 1. variables --------------------
## Using multiplication, create a variable `minutes_in_day` that is equal to the number of minutes in a day
minutes_in_day = 60 * 24
print("There are", minutes_in_day, "minutes in a day")
## Using multiplication, create a variable `hours_in_year` that is the number of hours in a year
hours_in_year = 24 * 365
print("There are", hours_in_year, "hours in a year")
## Create a variable `minutes_rule` that is a logical value (True/False) by logical operations
## It should be True if there are more minutes in a day than hours in a year, otherwise False
minutes_rule = False
if minutes_in_day > hours_in_year:
    minutes_rule = True
    print("There are more minutes in a day than there are hours in a year")
else:
    print("There are fewer minutes in a day than there are hours in a year")

## Compute the following a bit useful numbers.
## Assign the results to suitably named variables.
## 
## How many seconds are there in year?
seconds_in_year = 60 * minutes_in_day * 365
print("There are", seconds_in_year, "seconds in a year")

## How many seconds is a typical human lifetime?
typical_life = seconds_in_year * 70
print("A typical human lifetime is", typical_life, "seconds long")

## Age of the universe is 13.8 billion years.  What is it's age in seconds?
universe_age = seconds_in_year * 13800000000
print("The universe's age in seconds is", universe_age)
## Comment:
## If you find, based on timings on a scaled-down task, that your full task
## takes more than this many seconds on a fast computer,
## we can safely say that your code fails :-)


### ------------------------------ 2. working with lists, strings ------------------------------

## create a list 'things' that contains three things: mozarella, cinderella, salmonella
## print the list
things = ["mozarella", "cinderella", "salmonella"]
print("Things:", things)

## Capitalize the thing in the list that refers to a person.  Print the list
things[1] = things[1].capitalize()
print("Capitalize person:", things)
## Put the cheese-thing in all upercase and print the list.
things[0] = things[0].upper()
print("Uppercase cheese:", things)
## delete the disease element from the list.  Print the list.
things.pop()
print("Remove disease:", things)

## Create a list `movies` that contains the names of six movies you like
movies = ["To All the Boys I've Loved Before", "Best of Me", "Avengers Endgame", "Jumanji", "Spiderman", "A Cinderella Story"]
print("Movies:", movies)
## Create a list `top_three` that only contains the first three movies in the list.
## Use indexing and slicing!
top_three = movies[slice(0, 3, 1)]
print("Top three:", top_three)

### -------------------- 3. loops --------------------

## Using a loop, print out all the movies
print("Movies:")
for i in movies:
    print(i)
## Using a loop, create a new list `excited` that adds the phrase -
## " is a great movie!" to the end of each element in your movies list
##
## Hint: you need to concatenate strings
excited = []
for i in movies:
    excited.append(i + " is a great movie!")
print("Excited:", excited)

## Create a list `without_four` that has your first three movies, and your 5th and 6th movie.
without_four = top_three + movies[-2:]
print("Without four:", without_four)
## Create a list `numbers` that is the numbers 70 through 99
## note: `range()` does not give you a list.  Use a loop
## (don't use list comprehension here!)
numbers = []
for i in range(70, 100):
    numbers.append(i)
print("Numbers 70 through 99:", numbers)
## Using the built in len function, create a variable `length` that is equal to the length of your list
## `numbers`
length = len(numbers)
print("Length of numbers 70 through 99:", length)
## Use a loop to compute the mean value of the list.
total = 0
for i in numbers:
    total += i
average = total/length
print("Average of numbers 70 through 99:", average)
## Create a list `lower_numbers` containing numbers 60--69
lower_numbers = [i for i in range(60, 70)]
print("Numbers 60 through 69:", lower_numbers)
## Create a list `all_numbers` that combines your `lower_numbers` and `numbers` lists
all_numbers = lower_numbers + numbers
print("All numbers:", all_numbers)
## Use loop to compute sum of numbers 1..100
numbers_sum = 0
for i in range(1, 101):
    numbers_sum += i
print("Sum of 1-100:", numbers_sum)
## Compute 100! (product of numbers 1..100)
numbers_product = 1
for i in range(1, 101):
    numbers_product *= i
print("Product of 1-100:", numbers_product)
## create a list of 20 numbers, and extract the odd numbers using slicing
twenty_numbers = [i for i in range(1, 21)]
odd_numbers = twenty_numbers[slice(0, 19, 2)]
print("Odd numbers:", odd_numbers)
## create a list of 10 odd numbers (use loop and range, and it's arguments)
ten_odd = []
for i in range(1, 21, 2):
    ten_odd.append(i)
print("10 odd numbers:", ten_odd)
## -------------------- 4. dicts, sets

## create a dict of countries (keys) pointing to the corresponding capitals (value)
## (at least 5 countries/capitals).
countries_capitals = {"USA" : "Washington D.C.", "Canada": "Ottawa", "India": "New Delhi", "United Kingdom": "London", "France": "Paris"}
print("Countries and Capitals:", countries_capitals)
## Use a loop to create an 'inverted' dict with capital (keys) pointing to a
## corresponding country (value).
## Hint: create an empty dict and add capital-coutry pairs to it.
capitals_countries = {}
for i in countries_capitals:
    capital = countries_capitals[i]
    capitals_countries[capital] = i
print("Capitals and Countries:", capitals_countries)
## Using these two dicts, print a table of capital, country
## where the capitals are alphabetically ordered.
## 
## Example:
## Almaty, Kazakhstan
## Beijing, China
## ...
## Wellington, New Zealand
##
## Hint: create a sorted list of all capitals using the dicts
print("Sorted list of capitals:")
for i in sorted(capitals_countries.items()):
    print(i[0] + ", " + i[1])
## Here is a list of birthdays of 100 different people (the format is
## day of year).  How many different birthdays do we have?
birthdays = '''
206, 137,  97, 361,  62, 267, 296, 205, 183, 237, 221,  67, 265,
292, 129, 123, 104, 266, 236,  84, 124, 276, 109, 193,  31,  23,
306, 248, 195, 315,  82, 197,  11,   9, 274, 133, 143, 238, 292,
 75,  32, 257,  41,  96, 168, 295, 179,  70, 159,  19, 291, 267,
269, 250, 211, 184, 285, 187, 362, 338, 330, 104, 286, 256, 295,
 62, 347, 301, 224, 290, 279,  93, 167, 304,  80, 292, 356,  35,
320, 360,   7,  68, 192, 165, 248, 327, 290, 213,  63, 166, 206,
299,  72, 139, 256, 176, 200, 282, 193,   8
'''
## Hint: split this string into individual numbers, remove spaces, create a set
## split() method:
## "a b c".split() -> ['a', 'b', 'c']
birthdays = [int(x) for x in birthdays.split(',')]
print("Number of birthdays:", len(set(birthdays)))
## create a word frequency table using dicts that take a (looong)
## string, splits it into individual words, and counts the number of
## occurrencies of each word (and prints the result).  Let's ignore
## punctuation.
##
## your code should run over individual words and increase the counter
## for that word, stored in a list.  It has to check if a word exists
## in the dictionary, and if not, take an appropriate action.
##
## Hint: use the split() method:
## "I have no clue".split() -> ['I', 'have', 'no', 'clue']
## Hint2: convert everything to lower case

test_string = "This is my test string. It is looking for occurrences of repeating words."
test_string = test_string.replace(".", " ").lower()
split = test_string.split()
word_counts = {}
for i in split:
    value = word_counts.get(i, 0)
    word_counts[i] = value + 1
print("Word Frequency Table:")
for i in word_counts.items():
    print(i[0], i[1])

### -------------------- 5. Working with functions --------------------

## Write a function called `make_introduction` that takes in two arguments: name, and age. 
## This function should return a string value that says something like "Hello, my name is {name}, and I'm
## {age} years old".
## Note: it should _return_ a string, not print it!
def make_introduction(name, age):
    return "Hello, my name is " + name + ", and I'm " + str(age) + " years old"
## Create a variable `my_intro` by passing your variables `my_name` and `my_age` into your `make_introduction`
## function.  Always print the result!
my_name = "Simran"
my_age = 19
my_intro = make_introduction(my_name, my_age)
print(my_intro)
## Create a variable `casual_intro` by substituting "Hello, my name is ", with "Hey, I'm" in your `my_intro`
## variable.
## Hint: Check out str.replace and re.sub functions
casual_intro = my_intro.replace("Hello, my name is ", "Hey, I'm ")
print(casual_intro)
## Write a function `RemoveDigits` that will remove all digits (i.e., 0 through 9) from all elements in a
## *list of strings*.
def RemoveDigits(string_list):
    result = []
    for i in string_list:
        string = list(i)
        i = ""
        for x in string:
            if not x.isdigit():
                i = i + x
        result.append(i)
    return result 
## Demonstrate that your approach is successful by passing a list of courses and other objects to your function
## For example, RemoveDigits(["INFO 201", "CSE 142", "mps-803c"])
print('Digits removed from ["INFO 201", "CSE 142", "mps-803c"]:', RemoveDigits(["INFO 201", "CSE 142", "mps-803c"]))
test = RemoveDigits(["04hkho2", "l2ich", "79032hco4"])
print('Digits removed from ["04hkho2", "l2ich", "79032hco4"]:', RemoveDigits(["04hkho2", "l2ich", "79032hco4"]))

## Write an if/else statement that checks to see if your list has any digits left. If it does have
## digits, print "Oh no!", if it does not then print "Yay!"
stringify = ""
for i in test:
    stringify += i
if stringify.isalpha():
    print("Yay!")
else:
    print("Oh no!")
### -------------------- grading --------------------

## Q1: 3pt
## Q2: 6pt
## Q3: 12pt
## Q4: 7 (capitals) + 4 (birthdays) + 7 (word frequency)
## Q5: 11pt
