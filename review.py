# Review 1

# Mutable default argument - different my_list default value everytime the function called
# Fix: use None as default value, assign the empty list inside as mutable value. Keep it empty everytime the function called

def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []  
    my_list.append(value)
    return my_list

# mylst = add_to_list(123)
# print(mylst)
# my2lst = add_to_list(234)
# print(my2lst)


# Review 2  

# Can not display the argument directly
# Fix: use f-strings to display variables or use str.format() as well
def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."    #use f-strings to display variables
    # return "Hello, my name is {name} and I am {age} years old.".format(name = name, age = age)  # this is string format() method
# print(format_greeting('chris',13))


# Review 3

# Has issue related to how the count variable is incremented
# Fix: initialize the variable count first, and create new function to increament. Good for maintaining and understanding
class Counter:
    def __init__(self):
        self.count = 0
    def increment_count(self):
        self.count += 1
    def get_count(self):
        return self.count
    
# count = Counter()
# print(count.get_count())
# count.increment_count()
# print(count.get_count())
    

# Review 4 

# This is the thread unsafe counter
# TO change to thread safe counter, we can add a threading.Lock instance to the class to protect the count variable.

import threading
class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()       #initialize the lock as an instance variable

    def increment(self):
        with self.lock:             #we first acquire the lock then change the count
            self.count += 1

    def value(self):
        with self.lock:
            return self.count

    # def worker(counter):
    #     for _ in range(100000):
    #         counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# print(counter.value())


# Review 5 

# Wrong increment operator
# Fix: In the first condition of the if condition. The operator should be += to increase the integer
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1   # change from =+ to +=
        else:
            counts[item] = 1
    return counts
# lst= [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
# print(count_occurrences(lst))