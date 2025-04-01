def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


x = int(input("Enter the number of terms in the Fibonacci series: "))

if x <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    fibonacci(x)