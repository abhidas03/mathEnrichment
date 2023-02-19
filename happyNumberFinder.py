def happyFinder(number):
    num = number
    if (num == 1):
        return True
    elif (num == 4):
        return False
    else:
        digits = []
        sum = 0
        for i in str(num):
            digits.append(int(i))
        for value in digits:
            sum += value*value
        print(sum)
        num = sum
        return happyFinder(num)

print("This program sums the squares of each digit of the enterred number repeatedly until it reaches 1 or 4.")
print("All numbers will eventually reach 1 or 4. If the final number is 1, then the number is a happy number.")
while (1):
    num = input("Enter your number or 'quit' to stop: ")
    if (num.lower() == "quit"):
        print("Now quitting...")
        break
    if (not(num.isnumeric())):
        raise Exception("You must enter a number!")
    if (happyFinder(num)):
        print(f"{num} is a happy number! :)")
    else:
        print(f"{num} is not a happy number :(")


