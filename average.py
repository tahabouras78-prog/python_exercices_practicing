def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
numbers = []
for _ in range (5):
        n= float(input("Enter a number: "))
        numbers.append(n)

average = calculate_average(numbers)
print("The average is:", average)