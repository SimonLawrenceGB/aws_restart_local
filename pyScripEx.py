# First, we will take the input:
# lower_value = int(input("Please, Enter the Lowest Range Value: "))
# upper_value = int(input("Please, Enter the Upper Range Value: "))

lower_value = int(0)
upper_value = int(250)

for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            with open("results.txt", "a") as f:
                print(number, file=f)

print("Prime numbers have been saved to results.txt")
