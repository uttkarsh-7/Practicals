len = int(input("Enter The Length - "))
bre = int(input("Enter The Breadth - "))
hei = int(input("Enter The Height - "))

surface_area = 2*(len*bre+bre*hei+hei*len)
vol = (len*bre*hei)

print("The Surface Area Of Cuboid - ",surface_area)
print("The Volume Of Cuboid - ",vol)