#!/usr/bin/python3
Square = __import__('0-square').Square

# Test 1
my_square = Square(3)
print(type(my_square))  # <class '__main__.Square'>
print(my_square.__dict__)  # {'_Square__size': 3}

# Test 2: Check for 'size' attribute, should raise error
try:
    print(my_square.size)
except Exception as e:
    print(e)  # 'Square' object has no attribute 'size'

# Test 3: Check for '__size' attribute, should raise error
try:
    print(my_square.__size)
except Exception as e:
    print(e)  # 'Square' object has no attribute '__size'

