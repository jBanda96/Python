import random
#import antigravity

#Fibonacci serie
a, b = 0, 1

print("\n" * 2)
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
try:
    tableOf =  3 #int(input("Tabla de multiplicar del: "))

    print()
    for i in range(1, 11):
        print(tableOf, '*', i, '=' ,i*tableOf)

except ValueError as error:
    print(error, 'NaN')

#Números primos
print("\n\n")
for number in range(2, 10):
    if number % 2 == 0:
        print("Found an even number", number)
        continue
    print("Found a number", number)

#Print statement
print("\n" * 2)
print("-" * 40)
print("Hola", end=",\n")
print("-" * 40)

#For statement asking for input integers
print("\n" * 2)

lista = [int(x) for x in input('Ingresa números separados por espacio: ').split()]
print('Tipo:',
      type(lista),
      lista
      )

num = int(input("Ingresa un número: "))
str = str(input("Ingresa un string: "))
lst = list(input("Ingresa una lista: "))

print(type(num), type(str), type(lst))

#Vulnerabilities in input()
print("\n" * 2)
secret_number = random.randint(1,2)
print ("Pick a number between 1 to 500")
#print(f"Number to guess: {secret_number}")
print("Number to guess: {}".format(secret_number))
while True:
    res = int(input("Guess the number: "))
    if res==secret_number:
        print ("You win")
        break
    else:
        print ("You lose")
        continue

#Yields
print("\n" * 2)
def simpleGeneratorFunction():
    
    for i in range(1, 11):
        yield i * i

for value in simpleGeneratorFunction():
    print(f'Yield: {value}')

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

ask_ok('Do you really want to quit? ')
