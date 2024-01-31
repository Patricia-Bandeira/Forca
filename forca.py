#Importando biblioteca que gera palavra aleatória
import random

# Inicializa a variável lista_jogos do arquivo txt
lista_jogos = None

# Executa o conteúdo do arquivo txt
with open("lista.txt", "r") as arquivo:
    exec(arquivo.read())

#Limita tentativas
total_tentativas = 6

#Gerando palavra aleatoria
palavra_original = random.choice(lista_jogos).upper()
#Define como lista as letras que seram usadas
letras_usadas = []
#Define como lista as palavras usadas
palavras_usadas = []
#Definindo quantidade de letras
qtd_letras = len(palavra_original)
# Palavra mostrada é uma lista pois ai ela será mutável
palavra_mostrada = ["_"] * qtd_letras
#Retirando espaço para unir elementos (letras)
string_mostrada = "".join(palavra_mostrada)

#titulo
print('Bem-vindo ao Jogo da Forca')
print("_______________________________________")
print(f'Tema: Restaurantes - {palavra_original}')
print("_______________________________________\n")
print(palavra_mostrada)
print("_______________________________________")

#condicional 
while string_mostrada != palavra_original and total_tentativas > 0:

  letra_chutada = input("\nDigite uma letra: ").upper()

  #Verifica se o valor digitado é numerico
  while letra_chutada.isdigit():
    letra_chutada = input("\nNumero invalido! Digite uma letra: ").upper()


  #Se a quantidade de letras chutadas for 1 então
  if (len(letra_chutada)) == 1:
    #Enquanto a letra for repetida
    while letra_chutada in letras_usadas:
      letra_chutada = input("\nVocê ja usou esta letra! Digite outra letra: ").upper()
    #Quando a letra for digitada ela vai ser adicionada na lista de letras que ja foram
    letras_usadas.append(letra_chutada)

    # Se a letra pertence à palavra original
    if (letra_chutada in palavra_original):
      # faça ela aparecer na palavra mostrada
      for i in range(len(palavra_original)):
        if palavra_original[i] == letra_chutada:
          # trocar o underline da palavra_mostrada pela letra_chutada
          palavra_mostrada[i] = letra_chutada.upper()
    # Caso contrário 
    else:
      # o jogador perde uma vida
      total_tentativas -= 1


  # se for chutado mais de uma letra (palavra)
  else:
    #se a palavra digitada for igual termina 
    if letra_chutada == palavra_original:
      print("\nParabéns, você ganhou!")
      break
    #se a palavra estiver errada:
    else:
      letra_chutada = input("Não é essa palavra! Digite outra palavra ou letra: ")
      #loop continua se a palavra estiver errada
      continue

  
  print("\n_______________________________________")
  print(f"Tentativas restantes: {total_tentativas}")
  print("\n_______________________________________")
  print(f"Letras usadas: {letras_usadas}")
  print("\n_______________________________________")
  print(palavra_mostrada)
  print("_______________________________________")
  
  #Retirando espaço para unir elementos (letras) 
  string_mostrada = "".join(palavra_mostrada)

  # Condição de vitória
  if string_mostrada == palavra_original:
    print("\nParabéns, você ganhou!")
    break

  # Condição de derrota
  if total_tentativas <= 0:
    print("\nVocê perdeu... que pena! :(")
    break