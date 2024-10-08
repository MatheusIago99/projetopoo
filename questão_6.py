def calcular_salario_final(salario_inicial, ano_inicio, ano_fim):
    salario_atual = salario_inicial
    percentual_aumento = 1.5 / 100  

    for ano in range(ano_inicio + 1, ano_fim + 1):
        
        salario_atual *= (1 + percentual_aumento)
        
        
        percentual_aumento *= 2

    return salario_atual

def main():
    salario_inicial = 1000.00  
    ano_inicio = 1995
    ano_fim = 2025

    salario_final = calcular_salario_final(salario_inicial, ano_inicio, ano_fim)

    print(f"O salário do funcionário em {ano_fim} será: R$ {salario_final:.2f}")


main()