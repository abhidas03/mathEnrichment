print("This program sums the digits of the enterred number repeatedly and returns the result until it reaches 1 or 4. Type 'quit' to quit.")
while (1):
    num = input("Enter your number: ")
    if (num.lower() == "quit"):
        print("Now quitting...")
        break
    if (not(num.isnumeric())):
        raise Exception("You must enter a number!")
    while (num != 1 and num != 4):
        digits = []
        sum = 0
        for i in str(num):
            digits.append(int(i))
        for value in digits:
            sum += value*value
        print(sum)
        num = sum