numbers = input("Enter a list of numbers to find their mean, mode, and median: ")
numbers = [int(num) for num in numbers]

total_sum = sum(numbers)
amount = len(numbers)

if amount > 0:
    mean = total_sum/amount
    print("The mean is", mean)
else:
    print("You must enter a value")

frequency = {}
for num in numbers: 
    if num in frequency:
        frequency[num] += 1
    else: 
        frequency[num] = 1

max_freq = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_freq]  

if len(modes) == 1:
    print(modes[0])
else:
    print("The mode/modes is",modes)


if amount == 0:
    print("You must enter at least one number.")
else:
    # Step 5: Calculate the median
        if amount % 2 == 1:  # If the count is odd
            median = numbers[amount // 2]  # Get the middle element
            print("The median is", median)
        else:  # If the count is even
            mid1 = numbers[amount // 2 - 1]
            mid2 = numbers[amount // 2]
            median = (mid1 + mid2) / 2  # Average of the two middle numbers
            print("The median is", median)