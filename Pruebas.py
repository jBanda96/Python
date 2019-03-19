#Fibonacci serie
a, b = 0, 1

while a < 100:
    print(a, end=", ")
    a, b = b, a + b

#if statement
print()
number = 3 #int(input("\n\n\nInsert a number: "))
if number < 0:
    print("That's a negative number")
elif number == 0:
    print("Zero")
elif number == 1:
    print("Single")
elif number > 1:
    print("Other")

#for statement
print()
words = ['statement', 'cat', 'dog', 'defenestrate']
for word in words[:]:
    print(word, 'has', len(word), 'letters')

#Tabla de multiplicar
print("\n\n")
tableOf = int(input("Tabla de multiplicar del: "))
for i in range(1, 11):
    print(i*tableOf)
    if i == 4: break

#Números primos
print("\n\n")
for number in range(2, 10):
    if number % 2 == 0:
        print("Found an even number", number)
        continue
    print("Found a number", number)

#Print statement
print("Hola", end=",\n")
print("-" * 40)

#Función
print("\n\n")
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
