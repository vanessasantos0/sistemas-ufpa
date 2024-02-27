while True:
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")

    jogador_escolha = int(input("Digite o número: "))

    if jogador_escolha < 1 or jogador_escolha > 3:
        print("Escolha inválida. Tente novamente.")
        continue

    opcoes = ["Pedra", "Papel", "Tesoura"]
    jogador_escolha -= 1  # Ajusta para índice da lista
    
    from random import randint
    computador_escolha = randint (0,2)
    

  # --------------------------------------------------
  # FAÇA COM QUE A ESCOLHA DO COMPUTADOR SEJA ALEATÓRIA
  # --------------------------------------------------

    print("Você escolheu:", opcoes[jogador_escolha])
    print("O computador escolheu:", opcoes[computador_escolha])

    if jogador_escolha == computador_escolha:
        print("Empate!")
    elif (jogador_escolha == 0 and computador_escolha == 2) or \
         (jogador_escolha == 1 and computador_escolha == 0) or \
         (jogador_escolha == 2 and computador_escolha == 1):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != "s":
        break
