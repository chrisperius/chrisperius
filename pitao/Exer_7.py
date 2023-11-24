def mostrar_nome_sobrenome(nome):
   
    partes_nome = nome.split( )
    nome_usuário = partes_nome[0]
    sobrenome_usuario = " ".join(partes_nome[1:])
    nome_completo = nome.upper()
    tamanho_nome_completo = len(nome)
    
    print("Nome: "+nome_completo.lower())
    print("tem ",tamanho_nome_completo, " caracteres ")


    

mostrar_nome_sobrenome(input(" Escreva o seu nome completo "))