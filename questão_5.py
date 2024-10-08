def criar_tabela_precos():
    print("Lojas Quase Dois - Tabela de preços")
    for i in range(1, 51):
        preco = i * 1.99
        print(f"{i} - R$ {preco:.2f}")

def calcular_valor_total(quantidade):
    return quantidade * 1.99

def main():
    criar_tabela_precos()
    
    
    quantidade = int(input("\nDigite a quantidade de itens que o cliente está levando: "))
    
    if 1 <= quantidade <= 50:
        total = calcular_valor_total(quantidade)
        print(f"O total a pagar por {quantidade} item(s) é: R$ {total:.2f}")
    else:
        print("Quantidade inválida! Por favor, insira um número entre 1 e 50.")


main()