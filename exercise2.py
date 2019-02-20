names = ['Alex', 'Basil', 'Deborah']

def greeting(your_name):
    greet = ''
    for name in names:
        if your_name not in names:
            greet = "Who goes there?"
        else:
            greet = "Hello my name is {}!"
    print(greet.format(your_name))
    return

your_name = input("What is your name? ")
greeting(your_name)
