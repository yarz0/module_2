n = int(input("Введите число n от 3 до 20:"))
pass_ = []
for i in range(1, 21):
    for j in range((i + 1), 21):
        if i + j == n or n % (i + j) == 0:
            pass_.append(f"{i}{j}")
a = ''.join(pass_)
print(str(a))
