import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

N = int(input().strip())

B = 0


# INSERT YOUR CODE HERE
for i in range(N, 0, -1):
    B += i

print(B)

sys.stdout.close()