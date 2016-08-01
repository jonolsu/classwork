def factorial(n):
    if n == 1:
        return 1
    return (n * factorial(n - 1))


def fibonacci(limit):
    nums = []
    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        nums.append(current)
    return nums

def fibonacci_co(limit):
    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        yield current


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5), factorial(3), factorial(11)))

print('\nfibonacci via lists:\n')
for n in fibonacci(100000000000):
    print(n, end=', ')
print('\nfibonacci via yeild:\n')
for n in fibonacci_co(100000000000):
    print(n, end=', ')