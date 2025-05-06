class DataProcessor:
    inputN = 0
    numbers = []

    def dataInit(self):
        while True:
            try: 
                self.inputN = int(input("Please input a positive integer: "))
                if self.inputN <= 0 :
                    print("Input value is not positive, please try again.")
                else :
                    break
            except ValueError:
                print("Wrong input, please try agian.")


    def dataInsert(self):
        index = 0
        print(f"Input {self.inputN} numbers. ")
        while index < self.inputN:
            while True:
                try:
                    self.numbers.append(int(input(f"Input {index + 1} of {self.inputN} number(s)")))
                    break
                except ValueError:
                    print("Wrong input, please try again.")
            index += 1


    def dataSearch(self):
        while True:
            try:
                inputX = int(input("Please input a number you are searching for: "))
                break;
            except ValueError:
                print("Wrong input, please try again.")
        try:
            print(self.numbers.index(inputX)+1)
        except ValueError:
            print(-1)


### Test
dp = DataProcessor()
dp.dataInit()
dp.dataInsert()
dp.dataSearch()