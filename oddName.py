"""Emerson Baria"""
def main():
    name = get_name()
    name_print1=print_name(name)
    name_print3=print_name1(name)
    print (name_print1)
    print(name_print3)

def get_name():
    name = input('Please enter your name')
    return name

def print_name(name):
    print ("Frequency of 1")
    for i in range(1, len(name)):
        print(name[i])

def print_name1(name):
    print ('Frequency of 3')
    for i in range(1, len(name),3):
        print(name[i])

main()