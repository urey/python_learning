from TurtleWorld import *
import math
def square(t, num):
    for i in range(4):
        fd(t, num)
        lt(t)

def poly(t, num, n):
    angle = 360.0/n
    for i in range(n):
        fd(t, num)
        lt(t, angle)

def circle(t, r):
    angle = 1
    num = 2*r*math.sin(0.5/180)
    print num
    poly(t, num, 360)
        
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print bob
circle(bob, 100)

wait_for_user()

