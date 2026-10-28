import sys

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

si = (principal * rate * time) / 100
print("Simple Interest:", si)