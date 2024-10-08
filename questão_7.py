def calcular_divida(valor_divida):
    
    tabelas_juros = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }

    
    print("|{:^10}|{:^7}|{:^24}|{:^20}|".format("Dívida", "Juros", "Quantidade de Parcelas", "Valor da Parcela"))
    print("|" + "-" * 10 + "|" + "-" * 7 + "|" + "-" * 24 + "|" + "-" * 20 + "|")

    for parcelas, percentual_juros in tabelas_juros.items():
        
        juros = valor_divida * (percentual_juros / 100)
        valor_total = valor_divida + juros
        valor_parcela = valor_total / parcelas

    
        print("|{:^10.2f}|{:^7.2f}|{:^24}|{:^20.2f}|".format(valor_total, juros, parcelas, valor_parcela))

def main():
    
    valor_divida = float(input("Digite o valor da dívida: R$ "))
    calcular_divida(valor_divida)


main()