import  math
pi = math.pi
#Backup
#pi = 3.14
#radius = float(input("What's the radius of the circle?"))
#area = radius ** 2 * pi
#circumference = radius * 2 * pi
#print("the area of the circle is {0:.2f}cm\u00b2 and the circumference is {1:.2f}".format(area, circumference))


radius = float(input("What's the radius of the circle?"))
if(input('Vill du använda radien som heltal, Y/N?')=='Y'):
    radius = int(radius)
area = radius ** 2 * pi
circumference = radius * 2 * pi
print("the area of the circle is {0:.2f}cm\u00b2 and the circumference is {1:.2f}".format(area, circumference))
