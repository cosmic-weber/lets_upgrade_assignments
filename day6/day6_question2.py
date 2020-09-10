class Cone():
     def __init__(self, Radius, Height):
         self.radius = Radius
         self.height = Height

     def Volume(self):
         r = self.radius
         h = self.height
         V = int((3.14 * (r*r)*h) / 3)
         print("Volume is ", V)

     def Surface_area(self):
         r = self.radius
         h = self.height
         a = 3.14*r
         from math import sqrt
         b = (h*h) + (r*r)
         c = sqrt(b)
         d = r + c
         e = int(d*a)
         print("Surface area is: ", e)

p = int(input("Enter Radius: "))
q = int(input("Entre Height: "))
coco = Cone(p,q)
coco.Volume()
coco.Surface_area()
