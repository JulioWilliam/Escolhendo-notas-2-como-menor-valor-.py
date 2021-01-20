mae = [200, 100, 50, 20, 10, 5, 2]
#Variável mãe, serve como base de valores disponíveis para serem usados.

while True:
    ini = int(input("Digite um valor: ").strip())
    #ini: Valor base escolhido pelo usuário.
    cedused = []
    #cedused: irá armazenar os valores escolhidos pelo programa.
    cont0 = 0
    #Python não aceita valores de referência em listas dentro de um FOR(var[i + 1]).
    # Então criei uma variável armazenadora.

    for i, j in enumerate(mae):
        cont0 += 1
        while True:
            if ini == sum(cedused):
                break
            if j == 2 and j + sum(cedused) > ini:
                cedused.pop()
                cedused.pop()
            if sum(cedused) < ini:
                cedused.append(j)

            if ini == sum(cedused):
                break
            if j != 2:
                if ini < sum(cedused) + mae[cont0]:
                    cedused.pop()
                    break
    #O código, de maneira básica, funciona da seguinte maneira.
    # Irá fazer uma soma do maior para o menor.
    # Se o valor for menor que o digitado pelo usuário(ini)
    # Uma soma será feita. Caso o valor exceda o escolhido(ini),
    # ele deleta e passa para o próximo da lista(mae).
    # O diferencial desse programa é que ele analisa um passo a mais.
    # Ex: Digamos que o usuário escolha o valor 21.
    # Seria normal se uma das opções base(mae) tivesse o valor 1.
    # Como o menor valor base(mae) é 2,
    # em condições normais ele entraria em loop infinito, entre 20 e 22(10 + 5 + 5 + 2).
    # Para resolver esse problema,
    # o programa analise a soma de um índice(mae) a mais do que está sendo usado.
    # Assim ele pode decidir se aquele valor é o correto ou não.
    # Ex: valor escolhido pelo usuário: 21. (10 + 5 + 2 + 2 + 2 = 21)
    # Ele decidiu que se colocasse outro 5, o valor não bateria.
    # então mudou para o próximo índice(mae) que é o número 2.

    print(f"Notas usadas:")
    for k, l in enumerate(cedused):
        print(f"{l} ", end="")
        if k < (len(cedused) - 1):
            print("+ ", end="")
    print(f"= {ini}\n")

