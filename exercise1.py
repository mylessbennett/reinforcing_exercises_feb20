def sum_odd_num(numbers):
    sum_odd = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd

numbers = []
for num in range(1, 21):
    numbers.append(num)

sum_odd = sum_odd_num(numbers)
print(sum_odd)
