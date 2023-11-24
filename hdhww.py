nome = input("Digite seu nome")
pergunta = input( "{}. Você prefere Sol ou Lua?" .format(nome))
if pergunta == "Sol":
    print("Você gosta de se queimar?")
else:
    print("Vamos conversar sobre ela então")