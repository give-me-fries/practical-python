# bounce.py
#
# Exercise 1.5
height = 100
for i in range(10):
    height *= 0.6
    print(i+1, round(height, 4))