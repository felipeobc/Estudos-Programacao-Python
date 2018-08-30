import toy_story
import avatar
voltar = 1
while voltar == 1:

    escolha_filme = int(input("Escolha um filme: (1)Toy Story (2)Avatar: "))

    if escolha_filme == 1:
        print("Toy Story")
        opcao = int(input("Trailer(1) ou  Informação (2)"))
        if opcao == 1:
            toy_story.show_trailer()
        elif opcao == 2:
            print("informações")
            toy_story.show_infor()

    if escolha_filme == 2:
        print("Avatar")
        opcao = int(input("Trailer(1) ou  Informação (2)"))
        if opcao == 1:
            avatar.show_trailer()
        elif opcao == 2:
            print("informações")
            avatar.show_infor()
    voltar = int(input("deseja continuar (1)sim (2)Não"))

