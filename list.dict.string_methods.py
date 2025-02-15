# List/dict/string_methods
# List methods:
a = [15,8,9,'s','a','r',16]
# 1.append() -adds new element to the end of a list
a.append(5)
a.append('salom')

# 2.extend() -adds one list to other one
b = ['.',',','!']
a.extend(b)

c = ['(','^','_','^',')']
b.extend(c)

# 3.insert() - insert(position, element)
b.insert(1,'*')
b.insert(-1,'|')
# print(b)

# 4.copy()
a1 = a.copy()
b1 = b.copy()

# 5.count()
c = [1,1,1,2,2,2,2,3,3]
# print(c.count(1))
# print(c.count(3))

# 6.index()
# print(c.index(1))
# print(c.index(2))

# 7.pop() -pop(position)
a.pop(1)
# print(a)

c.pop(5)
# print(c)

# 8. remove()
b.remove('(')
# print(b)

a.remove('s')
# print(a)

# 9. clear()- removes all the elements from the list
# c.clear()

t = [1,2,3]
# t.clear()

# 10. reverse()
b.reverse()
c.reverse()

# print(b,c)

# 11.sort() - list.sort(reverse=True|False, key=myFunc)
d = ['a','s','d','e']
d.sort(reverse = True)
# print(d)

names = ['Temur','Asilbek','Ali']
def myfunc(e):
    return len(e)

names.sort(reverse = True, key = myfunc)
# print(names)

# Dictionary methods
car = {
    "brand":"KIA",
    "year": 2024,
    "electric": True,
    "colors": ["purple", "green", "blue", "black","white"]
}



# .keys() - Returns a list containing the dictionary's keys
# print(car.keys())

# values() - Returns a list of all the values in the dictionary
# print(car.values())

# .items() - Returns a list containing a tuple for each key value pair
# print(car.items())


#  update()- dictionary.update(iterable) - Updates the dictionary with the specified key-value pairs
car.update({"model":"K5"})
car.update({"state":"new"})
# print(car)

# get()-dictionary.get(keyname, value) -returns the value of the item with the specified key.
x = car.get("model")
# print(x)

x = car.get("engine","3.4l")
# print(x)

#  fromkeys() -dict.fromkeys(keys, value(for all keys)) - Returns a dictionary with the specified keys and value
k = ('1-key','2-key','3-key')
v = 11
d1 = dict.fromkeys(k,v)
# print(d1)

d2 = dict.fromkeys(k)
# print(d2)

# copy() - dictionary.copy()
d3 = d1.copy()
c = car.copy()

# pop() -dictionary.pop(keyname, defaultvalue)
d1.pop("1-key")
# print(d1)

d3.pop("2-key")
# print(d3)

# popitem() -  dictionary.popitem()
# The popitem() method removes the item that was last inserted into the dictionary. 
# In versions before 3.7, the popitem() method removes a random item.
c.popitem()
# print(c)

d2.popitem()
# print(d2)

# setdefault() - dictionary.setdefault(keyname, value)
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

x = car.setdefault("model")
# print(x)

x = car.setdefault("sale","50%")
# print(x)

# clear() Removes all the elements from the dictionary - dictionary.clear()
d1.clear()
# print(d1)

d2.clear()
# print(d2)

# String methods:
text = "hi, how are you doing today {name} {surname}?"
# print(text.capitalize())

t=text.upper()
# print(t)

# print(text.count('o'))

# print(t.casefold())
# print(text.encode())
# print(text.endswith('a'))
# print(text.startswith('h'))
# print(text.expandtabs(tabsize=20))
# print(text.find('a'))  #-returns the lowest index of searching element when it's found
# print(text.rfind("a"))   ##-returns the highest index of searching element when it's found
txt = 'How old are you {name}. I am {age}'.format(name='Olga',age=20)
# print(txt)
# print(text.format(name='John',surname='Rigas'))
# print(text.index('d'))
# print(text.rindex('d')) - #Searches the string for a specified value and returns the last position of where it was found
# print(txt.isalnum())     # Returns True if all characters in the string are alphanumeric
# print(text.isalpha())    #Returns True if all characters in the string are in the alphabet
# print(text.isascii())    #Returns True if all characters in the string are ascii characters
# print(text.isdecimal())    #Returns True if all characters in the string are decimals
# print(text.isdigit())      #Returns True if all characters in the string are digits
# print(text.isidentifier()) 
# print(text.islower())       
# print(text.isprintable())
# print(text.isspace())       #Returns True if all characters in the string are whitespace
tx=" "   
# print(tx.isspace())
# print(text.istitle()) 
# print(t.isupper()) 

tx = ("John","Riga","Oliver")
# x='_'.join(tx)      #joins all items in an iterable into a string,using separator
# print(x)        #result: John_Riga_Oliver

txt1="  banana    "
y=txt1.ljust(20,"O")         #string(should be single word).ljust(length, character), returns left justified version of a string
# print(y)  

# print(t.lower())
# print(txt1.upper())

# print(y.lstrip(" "))        #string.lstrip(characters), left trim version of a string
# print(txt1.rstrip("O"))         #right trim version of a string
# print(txt1.strip())             #Returns a trimmed version of the string

# print(text.maketrans("a","b","t"))  # str.maketrans(x, y, z), returns ascii codes of characters, but can be used to replace characters

# how to replace characters using maketrans()
mytable= str.maketrans("O","I")
# print(txt.translate(mytable))  #replacing I onto O

# print(txt.partition('Olga'))  #Returns a tuple where the string is parted into three parts
# print(txt.rpartition("are"))

# print(txt1.replace("a","o"))

# print(txt.split())      #Splits the string at the specified separator, and returns a list
# print(txt.rsplit()) 

# print(txt.splitlines( ))     #Splits the string at line breaks and returns a list


# print(txt.swapcase())       #Swaps cases, lower case becomes upper case and vice versa
# print(txt.title())          #Converts the first character of each word to upper case

# mydict = {97: 100}      #97 is unicode of 'a', 100 is unicode of 'd'
# print(txt.translate(mydict))      #string.translate(table), translating(or replacing) a to d

# print(txt1.strip().zfill(10))     #string.zfill(len). fills with zeros until the string is 10 character long









