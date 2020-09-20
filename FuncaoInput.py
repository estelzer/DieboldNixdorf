ttask = int(input("ttask: "))
umax = int(input("umax: "))

arquivo = open('input.txt', 'w')
arquivo = open('input.txt', 'r') # Abrir arquivo em modo leitura
conteudo = arquivo.readlines() # Verifica o conteúdo do arquivo
conteudo2 = arquivo.readlines()
conteudo.append(ttask)   # Adiciona conteúdo
conteudo2.append(umax)

arquivo = open('input.txt', 'w') # Em modo escrita
arquivo.write(str(conteudo,))    # Escrevendo o conteúdo criado.
arquivo.write("\n")
arquivo.write(str(conteudo2))

arquivo.close() # Fecha o arquivo