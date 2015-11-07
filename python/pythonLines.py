if __name__ == "__main__":
    main()

"""
operator
"""
 * unpacking/packing arguments --> sequence into list, list to sequence : they also work in reverse
 ** unpacking/paking dict into keyword arguments
 a ** b # pow(a,b)
not b # logical negation b



"""
type convert
"""
a =10 
aa = str(a) #  toString
int(aa) # to int

"""
loop
"""
for i in xrange(len(nums)):
	print i, nums[i]

for i in reversed(xrange(len(nums))):
	print i, nums[i]

for n in nums:
	print n
for index, item in enumerate(items):
	print (index,item)
for index, item in enumerate(items,start=1): # argument: start index start from 1, defualt = 0
	print(index,item)

"""
generator
"""
yield 
# turn the method into  generator -> when execute to yield instruction, 
# will have a interruption and return, for the next iteration, 
# it will start execute from the next instruction of yield
# return cannot be in generator method

"""
Integer , numbers
"""
-sys.maxint-1 # Integer.MIN_INTEGER
sys.maxint # Integer.MAX_INTEGER
max(x,y)
sys.float_info.max 
float("inf") # maximum number
float("-inf") #minimum number

"""
math
"""
x = abs(-1)

"""
String
"""
'abc'[::-1] # reverse string [begin:end:step]
string.replace(s, old, new) # replace 
string.replace(s,old,new,maxreplace) # replace old with new for the first maxreplace occurence of the old substring
string.strip() # remove leading and trailing whitespace
string.strip("abc") # remove leadning and trailing characters contains a,b,or c

string.split() # return a list of words split by  : \\+s* , a.k.a. white space
string.split("abc") # return a list of words using "abc" as the delimiter 
string.split("abc",10) # return a list of words using "abc" as the delimiter string, at most 10(maxsplit) splits are done, the return list has at most 10+1 elements
string.splitlines() # return a list of lines of string, breaking at line boudaries
string.partition("abc") # split the string at the first occurence of "abc", and return 3-tuple containing the part before "abc", the "abc", and the part after "abc"(separator)

string.startswith("abc") # string starts with "abc"
string.startswith("abc",1) # start with "abc" from start index 1
string.startswith("abc",1,2) # start with "abc" from start index 1 to end index 2
string.startswith(("abc","123")) # string starts with "abc" or "123", using tuple

string.swapcase()
string.upper()
string.lower()
string.title()
"""
filter(function,sequence) map(function,sequence) reduce(function,sequence,initial_value) 
"""

"""
Sets {}, Dictionaries {} hashmap hashset
"""
aSet = set(['a','b','c'])
aSet = set('abcdefg')
bSet = set('abdek')
a = {x for x in 'abcddefsdf' if x not in 'abc'}
diffSet = a - b  # unique letters in a: letters in a but not b
unionSet = a | b # letters in either a or b
bothSet = a & b # letters in both a and b 
notInBothSet = a ^ b # letters in a or b but not both

tel = {'x':1,'y':2}
tel['x'] = 100
del tel['x']
x in tes # containsKey
tel.keys()
tel.values()
map = dict([('x',1),('y',2)])
map = {x:x**2 for x in (2,4,6)}
for key,value in dict.iteritems():
	print key, value

# isEmpty : truth value testing
# https://docs.python.org/2/library/stdtypes.html#truth-value-testing
test_dict = {}
if not test_dict:
	print "Dict is Empty"
if not bool(test_dict):
	print "Dict is Empty"
if len(test_dict) ==0:
	print "Dict is Empty"

# remove
test_dict.pop("x",0)

"""
Collections.Counter
"""
cnt = collections.Counter(str1) # cnt is a dict : value is the count of char in str1
from collections import Counter
l.count("a") # l = ["a","b","c","a"]

"""
list []
"""
#list comprehensions: create list
squares = [x**2 for x in range(10)]
[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y ]
[row[i] for row in matrix for i in range(4)]

len(s)
map(function,iterable,...)
max(iterable,)
min(iterable)
next(iterator)

list.append(x) # append item:x in the end of the list
list.extend(L) #a[len(a):] = L
list.remove(x) # remove the first item from the list, rase an error if there is no such item
item = list.pop([i]) # remove the item at the given position in the list and return it
list.index(x) # search, find, return the index in the list of the first item whose value is x, raise an error is there is no such item
list.count(x) # return the number of times x appears in the list
list.sort(cmp=None,key=None,reverse=false)
list.reverse()

del a[0]
del a[2:4] # delete element of index=2,3, not include a[4]

"""
Stack
Queue
"""
stack = [3,4,5] 
stack.append(6)
stack.pop()

from collections import deque
queue = deque(['a','b','c'])
queue.append("ac")
queue.popleft()
"""
Sort Compare
"""
# list: argument: reverse
a = [1,2,3,4,5]
a.sort()  # ascending order, in-place sorting
b = sorted(a) # ascending order, return a new sorted list, not modifying the original list
b = sorted(a,reverse = True) # descending

# a list of Lists or Tuples: argument: key
l = [(1,2),(2,3),(3,4)]
def getKey(item):
	return item[1]
sorted(l, key = getKey)

# class object : __cmp__(self,other):
# hasattr(other,'age')
class Custom(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __cmp__(self,other):
		if hasattr(other,'age'):
			return self.number.__cmp__(other.number)
	def __repr__(self):
		return '{}: {} {}'.format(self.__class__.__name__, self.name, self,age)
def getKey(custom):
	return custom.age
customList = [Custom('tt',22), Custom('abc',100)]
sorted(customList, key=getKey)
sorted(curstomList,key=lambda custom : custom.age) # sort using lambda function
times.sort(key=lambda time: (time.val,time.t)) # sort by multiple attributes, key function (,,,)

"""
PriorityQueue
"""
import heapq
heapq.heappush(heap,item)
heapq.heappop(heap)
heapq.heapify(list)
heapq.heapreplace(heap,item) # pop and return the smalest item from the heap and also push the new item


"""
syntax sugar
"""
# matrix
grid # type grid: List[List[int]]
row_sum = map(sum,grid) # get the sum by row of a matrix
col_sum = map(sum,zip(*grid)) # get the sum by col of a matrix

# zip
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y) # zipped [(1,4),(2,5), (3,6)]
# x==x2 and y==y2 zip() in conjuction with the * operator can be used to unzip a list
# *zipped   zip((1,4),(2,5),(3,6))
x2, y2 = zip(*zipped) 
