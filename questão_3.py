def eh_numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Digite um número inteiro: "))
    
    if eh_numero_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")


main()