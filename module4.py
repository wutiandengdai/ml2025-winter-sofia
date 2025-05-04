### 1. asks the user for input N (positive integer) and reads it
while True:
    try: 
        inputN = int(input("Please input a positive integer: "))
        if inputN <= 0 :
            print("Input value is not positive, please try again.")
        else :
            break
    except ValueError:
        print("Wrong input, please try agian.")


### 2. Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
numbers = []
index = 0
print(f"Input {inputN} numbers. ")
while index < inputN:
    while True:
        try:
            numbers.append(int(input(f"Input {index + 1} of {inputN} number(s)")))
            break
        except ValueError:
            print("Wrong input, please try again.")
    index += 1


### 3. outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
while True:
    try:
        inputX = int(input("Please input a number you are searching for: "))
        break;
    except ValueError:
        print("Wrong input, please try again.")
try:
    print(numbers.index(inputX)+1)
except ValueError:
    print(-1)