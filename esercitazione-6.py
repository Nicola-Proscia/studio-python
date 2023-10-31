# dato un valore a n di che è starno sè è dispari sè è compreso tra 2 e 5 stampa not weird sè è compreso tra  6 e 20 weird maggiore di 20 not weird

n = 2

if n % 2 == 0:
    print("strano")
elif n >= 2 and n <= 5:
    print("not weird")
elif n >= 6 and n <=20:
    print("weird")
elif n > 20:
    print("not weird")
            