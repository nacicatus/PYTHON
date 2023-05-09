# Little Boxes

# A useful box for storing whole numbers:
score = 0
print(score)

# Another one for storing fractions:
hogwarts_platform = 9.75
print(hogwarts_platform)

# Two boxes for storing text
king = "Charles"
queen = "Camilla"
print("King " + king)

# A List
shopping_list = ['Eggs', 'Bacon', 'Milk', 'Bananas', 'Broccoli']
# You can add to the list by .append or .insert
shopping_list.append('Napkins') # adds it to the end of the list
shopping_list.insert(1, 'Chips') # adds it to the position 1

print(shopping_list[4])


# A Dictionary has key-value pairs, separated by commas, in curly braces
prices = {
    'Eggs': 1440, 
    'Bacon': 3200, 
    'Milk': 280,
    'Bananas': 499, 
    'Broccoli': 300
    }

# You can add to a dictionary by assigning a value to a key
prices['Jam'] = 500

print(prices)


# A tuple is just stuff thrown together without braces and such (but it is in order)
hippie_stuff = 'beads', 'guitar', 420, 'incense', 'tie-dye shirt', 'sandals'
print(hippie_stuff[1])

# A Set has curly braces like a dictionary, but no key-value pairs, 
# and is not ordered, i.e. its elements are just thrown together, duplicates eliminated
fruits = {'apple', 'banana', 'cherries', 'grapes', 'apple'}
print(fruits) # will display the contents of the set in any order, even a different order every run

