def verificar_respostas(gabarito):
    acertos = 0
    for i in range(10):
        resposta = input(f"Qual a sua resposta para a questão {i + 1}? ").strip().upper()
        if resposta == gabarito[i]:
            acertos += 1
    return acertos

def main():
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    resultados = []

    while True:
        print("\n--- Sistema de Verificação de Nota ---")
        acertos = verificar_respostas(gabarito)
        resultados.append(acertos)

        
        continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if resultados:
        maior_acerto = max(resultados)
        menor_acerto = min(resultados)
        total_alunos = len(resultados)
        media_notas = sum(resultados) / total_alunos

        print("\n--- Resultados Finais ---")
        print(f"Maior Acerto: {maior_acerto}")
        print(f"Menor Acerto: {menor_acerto}")
        print(f"Total de Alunos que utilizaram o sistema: {total_alunos}")
        print(f"Média das Notas da Turma: {media_notas:.2f}")
    else:
        print("Nenhum aluno utilizou o sistema.")


main()
