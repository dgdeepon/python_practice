
# 1
print("Hello, World!")

# 2
variable1,variable2,variable3,variable4,variable5,variable6,variable7,variable8=10,3.5,True,"hello",[25,33,53,75],("name","age","Address"),{"language":"python","year":1991},{"arjun","aman","sandip"}

print(type(variable2),variable2)

# 3
new_list=list(range(1,11))

new_list.append(3)
new_list.append(12)
new_list.pop(0)
new_list.remove(12)

new_list.sort()

print(new_list)

# 4
arr=[10, 20, 30, 40]

total=sum(arr)

print("sum:{} \naverage:{}".format(total,total/len(arr)))

# 5
str="Python"[::-1]
print(str)

# 6
new_str="Hello"
vowel=['a','e','i','o','u']
count=0

for i in new_str:
  if i in vowel:
    count+=1


print(count)

# 7
def isPrime(num):
  no=0
  if num < 2 :
    return False
    
  for i in list(range(1,num+1)):
    if num%i==0 :
      no+=1
  return no == 2    

print(isPrime(6))

# 8
def factorial(num,result=1) :
    if num<=0:
      return result
    result=result*num
    num=num-1  
    return factorial(num,result)

print(factorial(5))

# 9
def fibonacci(num):
  result=[0,1]
  while len(result)<num :
    number=result[-1]+result[-2]
    result.append(number)
    
  return result

print(fibonacci(5))

# 10
new_no = [x**2 for x in range(1, 11)]
print(new_no)

  
import math

# 1

def patternBuild(num):
  pattern=''
  i=1
  while i<=num:
    pattern+='{}'.format(i)
    i+=1
    print(pattern)


patternBuild(5)

# 2
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
  if i>500:
    break
  elif i>150:
    continue
  elif i%5==0:
    print(i)

# 3
s1 = "Ault"
s2 = "Kelly"

length=math.floor(len(s1)/2)

s3=s1[:length]+s2+s1[length:]

print(s3)

# 4
str1 = "PyNaTive"

lower=[i for i in str1 if i==i.lower()]
upper=[i for i in str1 if i==i.upper()]

result="".join(lower+upper)


print(result)

# 5
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

min_length=min(len(list1),len(list2))

ans=[]

for i in range(min_length):
  ans.append("{}{}".format(list1[i],list2[i]))


if len(list1) > min_length :
  ans.extend(list1[min_length:])
else :
  ans.extend(list2[min_length:])

print(ans)

# 6
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
ans=[]

for i in list1:
  for j in list2:
    ans.append("{} {}".format(i,j))

print(ans)

# 7
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i in range(len(list1)):
    print(list1[i],list2[i])


# 8
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

obj={}

for i in employees:
  obj[i]=defaults

print(obj)

# 9
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

obj={}

for i in keys:
  obj[i]=sample_dict[i]

print(obj)

# 10
tuple1 = (11, [22, 33], 44, 55)

list1=list(tuple1)

list1[1][0]=222

tuple1=tuple(list1)

print(tuple1)


# 1
list1=[("John", 25), ("Jane", 30)]

ans=''

for i in list1:
  ans+=" {} is {} years old.".format(i[0],i[1])

print(ans)

# 2
obj={}

obj['John']=25

print(obj)

obj['John']=26

print(obj)

del obj['John']

print(obj)

# 3
def mainFunction(lists,target):
  obj={}
  for index, item in enumerate(lists):
    new_target=target-item
    if new_target in obj:
      print([obj[new_target],index])
      return
    obj[item]=index

list1=[2, 7, 11, 15]

mainFunction(list1,9)

# 4

str="madam"


def isPalindrome(str):
  new_str=str
  str=[letters for letters in str]
  str.reverse()
  str="".join(str)
  return str==new_str

print(isPalindrome(str))

# 5

list1=[64, 25, 12, 22, 11]

for i in range(len(list1)):
  index=i
  for j in range(i+1,len(list1)):
    if list1[index] > list1[j] :
      index=j
  list1[index],list1[i]=list1[i],list1[index]


print(list1)

# 6
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.put(item)

    def pop(self):
      
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

      
        if not self.q1.empty():
            popped_item = self.q1.get()
        else:
            popped_item = None

      
        self.q1, self.q2 = self.q2, self.q1

        return popped_item


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())


# 7
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 8
file=open("input.txt",'r')
reading=file.read()
words=reading.split()
number_of_words=len(words)
# print(number_of_words)
new_file=open("output.txt",'a')
new_file.write(f"{number_of_words}")
new_file.close()
file.close()

# 9
def division(num1,num2):
  try:
    return num1//num2
  except ZeroDivisionError:
    return "Cannot divide by zero."

print(division(5,5))
