fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci series is:")
for i in range(5):
    print(fibonacci(i))