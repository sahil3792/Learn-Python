#Python Multi-Line Statements
'''Statements in Python typically end with a new line. 
Python does, however, allow the use of the line 
continuation character (\) to denote that the line 
should continue. For example −'''

item_one = "apple"
item_two = "Grapes"
item_three = "mango"

total = item_one + \
        item_two + \
        item_three

print(total)

'''Statements contained within the [], 
{}, or () brackets do not need 
to use the line continuation 
character. For example following statement 
works well in Python −'''

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)