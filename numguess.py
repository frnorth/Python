import random

def main():
    smaller=int(input("Enter the smaller number: "))
    larger=int(input("Enter the larger number: "))
    mynum=random.randint(smaller,larger)
    count=0
    while True:
        count+=1
        usernum=int(input("Enter your guess: "))
        if usernum < mynum:
            print("Too small")
        elif usernum > mynum:
            print("Too large")
        else:
            print("Yeah!",count,"times")
            break

if __name__=="__main__":
    main()

