def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci = fibonacci_sequence(n)
print(fibonacci)
