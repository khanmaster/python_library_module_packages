# What are modules?

# A module is a piece of software that delivers a piece of functionality

# Let's learn by an example of a module called os which us very useful for getting system information

# first iteration
# import os
#
# working_directory = os.getcwd()
# # getcwd() method gives you the current working directory
#
# print(working_directory)
# # output will our current working directory

# 2nd iteration - comment out the above code
from os import *
import math, datetime, sys

def return_user_id():
    print(os.getcwd())

def operating_system_information():
    print(os.cpu_count())

print(math.remainder(1, 5))

print(datetime.date.today())

print(sys.path)

# we will create another file called use_os_module in the same directory
# we will import this file in use_os_module and

# print(working_directory)
# output will our current working directory

# return_user_id()
#
# print(working_directory)
