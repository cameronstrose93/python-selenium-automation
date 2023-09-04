# Level 1
def foo_bar(n: int):
    for i in range(1, 101):

        #  Check if the number is divisible by 3 and print 'Bar'
        if i % 3 == 0:
            print('Bin')
        elif i % 7 == 0:
            print('Go')
        elif i % 3 == 0 and i % 7 == 0:
            print('Bingo')
        else:
            print(i)


foo_bar(100)


def sum_numbers(n: int):
    # Initialize the variable 'final_sum' and set it to 0 initially
    final_sum = 0

    # Use a loop to iterate over numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Count the sum of digits for each iteration
        final_sum += i
        # Return the 'final_sum' as the result
        return final_sum


sum_numbers(6)
print('')


# Level 2

def find_max(a: int, b: int, c: int):
    result = max(a, b, c)
    print(result)


find_max(2, 3, 9)
print('')


def leap_year(year: int):
    if year % 4 == 0:
        print('Leap Year')
    elif year % 100 == 0:
        print('Not Leap year')
    elif year % 400 == 0 and year % 100 == 0:
        print('Leap Year')
    else:
        print('Invalid')


leap_year(2020)
print('')


# Level 3

def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        next_num = fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2]
        # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(next_num)

    print(fib_sequence)


generate_fibonacci_sequence(9)

