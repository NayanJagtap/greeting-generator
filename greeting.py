import datetime

def greet(name):
    current_hour=datetime.datetime.now().hour
    if 5 <=current_hour <12:
        greeting = "Good Morning "
    elif 12<=current_hour<18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    return f"{greeting},{name}!"

if __name__ == "__main__":
    print(greet("Friend"))

