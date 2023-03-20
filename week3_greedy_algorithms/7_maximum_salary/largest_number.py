from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    yourSalary = ""
    while numbers:
        maxNumber = numbers[0]
        for number in numbers:
            if is_better(number, maxNumber):
                maxNumber = number
        yourSalary += str(maxNumber)
        numbers.remove(maxNumber)
    return yourSalary

def is_better(number,max_number):
    return int(number+max_number) > int(max_number+number)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
