import random

def main() :
    for i in range(0, 3):
        spin()


def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15) :
        output = "Cherries"
    elif (rand_num > 10) :
        output = "Orange"
    elif(rand_num > 5) :
        output = "Plum"
    elif(rand_num > 2) :
        output = "Bell"
    elif (rand_num > 1) :
        output = "Melon"
    else:
        output = "Bar"
    
    print(output, end = " ")

main()