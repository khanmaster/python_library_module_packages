# install python package requests
# on command line run - pip install requests
# verify it with - pip -V

import requests

requests_bbc = requests.get("http://www.bbc.co.uk/")


# print(requests_bbc.status_code)
# print(requests_bbc.headers)
# print(requests_bbc.content)

# second iteration to simplify our code and make it reusable

# def check_response_code():
#     if requests_bbc.status_code == 200:
#         print("Response successful")
#     elif requests_bbc.status_code == 404:
#         print(" Sorry page not found")
#     else:
#         print(" Opps some went wrong")
# print(check_response_code())

# 3rd iteration to apply best practice
def check_response_code():

    if requests_bbc:
        print("Response successful")
    elif requests_bbc:
        print(" Sorry page not found")
    else:
        print(" Opps some went wrong")

print(check_response_code())

# requests goes one step further in simplifying this process for us.
# If you use a request_bcc instance in a conditional expression,
# it will evaluate to True if the status code was between 200 and 400, and False otherwise.
# Therefore, you can simplify the last example by rewriting the if statement as above: