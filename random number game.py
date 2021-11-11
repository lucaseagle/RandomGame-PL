from random import randint

def input_check(sentence):
    while (True):
        try:
            n = int(input(sentence))
            return n
        except ValueError:
            print("Nieprawidłowa liczba!")

while (True):
    print("### ZGADNIJ, JAKĄ LICZBĘ MAM NA MYŚLI! ###\n")

    first = input_check("Podaj dolny zakres, z jakiego będzie losowana liczba: ")
    while (True):
        last = input_check("Podaj górny zakres, z jakiego będzie losowana liczba: ")
        if (not last > first): print(f"Liczba musi być większa niż {first}!")
        else: break
        
    number = randint(first, last)
    counter = 0
    while (True):
        counter +=1
        guess = input_check("Jaką liczbę mam na myśli? ")
        if (guess == number):
            print(f"\nZgadza się! Udało Ci się w {counter} próbie!\n")
            break
        if (guess < number): print("\nMoja liczba jest większa :-)")
        if (guess > number): print("\nMoja liczba jest mniejsza :-)")
        print("Spróbuj jeszcze raz!\n")

    while (True):
        next_game = input("Czy chcesz zagrać jeszcze raz? (t/n): ").lower()
        if (next_game == 'n'): quit()
        if (next_game != 't'): print('Wpisz: \'t\' lub \'n\'! ')
        else: break





