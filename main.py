import math
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def rotate(self, origin, theta):
        xr = math.cos(theta) * (self.x - origin.x) - math.sin(theta) * (self.y - origin.y) + origin.x
        yr = math.sin(theta) * (self.x - origin.x) + math.cos(theta) * (self.y - origin.y) + origin.y
        return Point(xr, yr)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def length(self):
        return (self.x**2 + self.y**2)**(1/2)

class Tail:
    def __init__(self, n):
        self.n = n
        self.h = 20
        self.l = [i*self.h for i in range(0, n)]
        self.r = [i*self.h for i in range(0, n)]
        self.w = 10
        self.d = 2


    def turn_left(self, i):
        self.l[i] -= self.d
        self.r[i] += self.d

    def turn_right(self, i):
        self.l[i] += self.d
        self.r[i] -= self.d

    def get_points(self):
        w = self.w
        n = self.n
        left = [Point(0, i) for i in range(n)]
        right = [Point(w, i) for i in range(n)]
        left[0] = Point(-w/2, 0)
        right[0] = Point(w/2, 0)
        for i in range(1, n):
            l = self.l[i] - self.l[i-1]
            r = self.r[i] - self.r[i-1]
            print(l, r)
            A = left[i-1]
            B = right[i-1]
            alpha = (r - l) / w
            if r > l:
                R = l / alpha
                O = A + (A - B) * R / w
                left[i] = A.rotate(O, alpha)
                right[i] = B.rotate(O, alpha)
            if r < l:
                R = l / -alpha
                O = B + (B - A) * R / w
                left[i] = A.rotate(O, alpha)
                right[i] = B.rotate(O, alpha)
            if r == l:
                left[i] = A + (B.rotate(A, math.pi / 2) - A) / w * l
                right[i] = B + (A.rotate(B, -math.pi / 2) - B) / w * l

            print((left[i]-left[i-1]).length(), (right[i]-right[i-1]).length())


        return left, right

def draw(tail):
    left, right = tail.get_points()
    plt.axis('equal')
    plt.plot([e.x for e in left], [e.y for e in left], color="Red", linestyle='-', marker='o')
    plt.plot([e.x for e in right], [e.y for e in right], color="Blue", linestyle='-', marker='o')
    plt.title('Tail')
    plt.grid()
    plt.show()



if __name__ == '__main__':
    tail = Tail(4)

    for i in range(7):
        tail.turn_left(2)

    for i in range(7):
        tail.turn_left(3)




    draw(tail)

