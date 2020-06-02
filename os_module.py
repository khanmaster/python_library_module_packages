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
import os

# now we will create our own methods and utilise built in methods to get best out of python
working_directory = os.getcwd()

# Let's create a method find out the user id
def return_user_id():
    print(os.getuid())

# find out the os info

def operation_system_information():
    print(os.uname())


# we will create another file called use_os_module in the same directory
# we will import this file in use_os_module and

#print(working_directory)
# output will our current working directory


# return_user_id()
# operating_system_information()
#
# print(working_directory)