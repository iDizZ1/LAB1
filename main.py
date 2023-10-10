a = int(input())
b = int(input())
c = int(input())
D = b**2-4*a*c
if D < 0:
   print("Корней нет")
if D == 0:
   print("корень = ", -b/(2*a))
if D > 0:
   print("1 корень = ", (-b+D**0.5)/(2*a))
   print("2 корень = ", (-b - D ** 0.5) / (2 *a))