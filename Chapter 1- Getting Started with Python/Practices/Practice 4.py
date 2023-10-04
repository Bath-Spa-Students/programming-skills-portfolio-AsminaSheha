#Compute the area of a triangle

#three sides of the triangle is a , b and c:
a= float(input('enter first side: '))
b= float(input('enter second side: '))
c= float(input('enter third side: '))

# calculate the semi-perimeter  
s = (a + b + c) / 2  

# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   