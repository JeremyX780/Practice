# my_module.py

def add_numbers(a, b):
    print (f"I'm in my Module add number{__name__} ") 
    return a + b + a%2


if __name__ == '__main__':
    print (f"I'm im my Module Main.{__name__}")
    add_numbers(2,3)