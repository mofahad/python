Dictionaries, Oh Lovely Dictionaries
N
ow I have to hurt you with another container you can use, because once you learn this con-
tainer, a massive world of ultra- cool will be yours. It is the most useful container ever: the
dictionary.
Python calls them “dicts.” Other languages call them “hashes.” I tend to use both names, but it
doesn’t matter. What does matter is what they do when compared to lists. You see, a list lets you
do this:
>>> things = ['a', 'b', 'c', 'd']
>>> print things[1]
b
>>> things[1] = 'z'
>>> print things[1]
z
>>> print things
['a', 'z', 'c', 'd']
>>>
You can use numbers to “index” into a list, meaning you can use numbers to fi nd out what’s in
lists. You should know this about lists by now, but make sure you understand that you can only
use numbers to get items out of a list.
What a dict does is let you use anything, not just numbers. Yes, a dict associates one thing to
another, no matter what it is. Take a look:
>>>
>>>
Zed
>>>
36
>>>
74
>>>
>>>
San
>>>
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = "San Francisco"
print stuff['city']
Francisco
You will see that instead of just numbers we’re using strings to say what we want from the stuff
dictionary. We can also put new things into the dictionary with strings. It doesn’t have to be
strings though. We can also do this:
www.it-ebooks.infoDICTIONARIES, OH LOVELY DICTIONARIES
133
>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print stuff[1]
Wow
>>> print stuff[2]
Neato
>>> print stuff
{'city': 'San Francisco', 2: 'Neato',
'name': 'Zed', 1: 'Wow', 'age': 36,
'height': 74}
>>>
In this code I used numbers, and then you can see there are numbers and strings as keys in the dict
when I print it. I could use anything—well, almost, but just pretend you can use anything for now.
Of course, a dictionary that you can only put things in is pretty stupid, so here’s how you delete
things, with the del keyword:
>>> del stuff['city']
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'Zed', 'age': 36, 'height': 74}
>>>
We’ll now do an exercise that you must study very carefully. I want you to type this exercise in and
try to understand what’s going on. Take note of when I put things in a dict, get from them, and
all the operations I use here.
ex39.py
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
# create a mapping of state to abbreviation
states = [
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
]
# create a basic set of states and some cities in them
cities = [
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
]
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
www
