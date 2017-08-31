from secrets import randbelow
def numberGen(randLen):
    randNum = 0

    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    numbers = '1 2 3 4 5 6 7 8 9 0'
    special = '! @ # $ % ^ & * ( ) { } [ ] < > , . / ? ` ~ - _ = +'
    char = []
    randChars = []

    alphabet = alphabet.split(' ')
    numbers = numbers.split(' ')
    special = special.split(' ')
    special.append(' ')

    for a in alphabet:
        char.append(a)

    for n in numbers:
        char.append(n)

    for s in special:
        char.append(s)

    
    for i in range(0, randLen):
        randNum = randbelow(len(char))
        randChars.append(char[randNum])

    for r in randChars:
        print(r, end='')
    print( )

def loop():
    while True:
        randLen = input('How long is your random char going to be? ')
        try:
            randLen = int(randLen)
        except:
            try:
                randLen = str(randLen)
                randLen = len(randLen)
            except:
                break
        numberGen(randLen)

def main():
    loop()

main()
