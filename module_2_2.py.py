first =  int(input('Введите 1е число '))
second = int(input('Введите 2е число '))
third =  int(input('Введите 3е число '))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
