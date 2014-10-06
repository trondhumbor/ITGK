
def fibonacci(n):
    numbers = [0, 1]
    for i in range(2, n + 1):
        numbers.append(numbers[-2] + numbers[-1])
    return numbers

if __name__ == "__main__":
    for x, z in enumerate(fibonacci(10)):
        print("n:", x, "f(n):", z)