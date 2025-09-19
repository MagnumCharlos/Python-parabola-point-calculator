# automatically gives you the coordinates of a parabola
x = 1 #the x coordinate
y = 1 # the y coordinate
a = int(input("a =")) #a is the factor of x
x_exp = int(input("exponent of x =")) #the exponent of x
c = int(input("c =")) #the startpoint
forloop = int(input("how many loops?"))


for i in range(1, forloop):
  x = y ** x_exp
  print(f"y({y}) = ", a * x + c)
  y = y + 1