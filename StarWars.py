import os
import time
import sys

# Limpa a tela (funciona no Pydroid e Linux)
os.system('clear')  # Use 'cls' se estiver no Windows

mensagem = """A galáxia está em perigo!Antes de pilotar a Millennium Falcon ou empunhar seu sabre de luz,
você precisa provar seu valor.

Bem-vindo ao *Quiz Star Wars*!

Prepare-se para enfrentar perguntas que até o Conselho Jedi teria dificuldade.

Que a Força esteja com você.
"""

# Função para imprimir com efeito de digitação
def digitar(texto, delay=0.10):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Centraliza e imprime linha por linha com efeito
for linha in mensagem.split('\n'):
    digitar(linha.strip().center(5)) 

input("\nAperte Enter para começar!\n")

# Pergunta 1

print("1) Quem é o pai de Luke Skywalker?")
print("1) Obi-Wan Kenobi, 2) Han Solo, 3) Mace Windu, 4) Anakin Skywalker\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 4 else 0
print("Correto!\n" if resposta == 4 else "Errado! A resposta certa é: Anakin Skywalker\n")

# Pergunta 2

print("2) Planeta natal de Anakin Skywalker?")
print("1) Naboo, 2) Coruscant, 3) Tatooine, 4) Endor\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 3 else 0
print("Correto!\n" if resposta == 3 else "Errado! A resposta é Tatooine\n")

# Pergunta 3

print("3) Quem matou o Conde Dookan?")
print("1) Yoda, 2) Anakin Skywalker, 3) Obi-Wan Kenobi, 4) Palpatine\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 2 else 0
print("Correto!\n" if resposta == 2 else "Errado! A resposta é Anakin Skywalker\n") 

# Pergunta 4

print("4) O que é a Estrela da Morte?")
print("1) Uma lua gigante, 2) Uma estação espacial com capacidade de destruir planetas, 3) Um caça TIE, 4) O planeta natal dos Sith\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 2 else 0
print("Correto!\n" if resposta == 2 else "Errado! A resposta é Uma estação espacial com capacidade de destruir planetas\n")

# Pergunta 5

print("5) Qual é o nome da princesa que lidera a Aliança Rebelde?")
print("1)Leia Organa, 2) Padme Amidala, 3) Rey, 4) Ahsoka Tano\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 1 else 0
print("Correto!\n" if resposta == 1 else "Errado! A resposta é Leia Organa\n")

# Pergunta 6

print("6) Quem treinou Luke Skywalker em Dagobah?")
print("1) Obi-Wan Kenobi, 2) Mace Windu, 3) Qui-Gon Jinn, 4) Mestre Yoda\n")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 4 else 0
print("Correto!\n" if resposta == 4 else "Errado! A resposta certa é: Mestre Yoda\n")

# Pergunta 7

print("7) Quem matou Jabba the Hutt?")
print("1) Han Solo, 2) Luke Skywalker,3) Chewbacca, 4)Princesa Leia")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 4 else 0
print("Correto!\n" if resposta == 4 else "Errado! A resposta certa é: Princesa Leia\n")

# Pergunta 8

print("8) Qual o nome do mentor de Obi-Wan Kenobi?")
print("1) Qui-Gon Jinn, 2) Palpatine,3) Lando Calrissian, 4) Bail Organa")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 1 else 0
print("Correto!\n" if resposta == 1 else "Errado! A resposta certa é: Qui-Gon Jinn\n")

# Pergunta 9

print("9) Como são chamados os soldados do Império ?")
print("1) Jedi, 2) Stormtroopers, 3) Caçadores de recompensa, 4) Rebeldes")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 2 else 0
print("Correto!\n" if resposta == 2 else "Errado! A resposta certa é: Stormtroopers\n")

# Pergunta 10

print("10) Qual desses personagens sobrevive até o final do Episódio VI?")
print("1) Darth Vader, 2) Yoda, 3) Obi-Wan Kenobi, 4)Luke Skywalker")
resposta = int(input("Digite sua resposta: "))
pontuacao += 1 if resposta == 4 else 0
print("Correto!\n" if resposta == 4 else "Errado! A resposta certa é: Luke Skywalker\n")

# Resultado final com efeitos

import time

print("\nCalculando seu nível de conexão com a Força...\n")
time.sleep(2)
print(f"Você acertou {pontuacao} de 10 perguntas!\n")
time.sleep(1.5)

if pontuacao == 10:
    mensagem_final = "Impressionante! Você é um verdadeiro Mestre Jedi. Yoda ficaria orgulhoso!"
elif 7 <= pontuacao < 10:
    mensagem_final = "Muito bem, jovem padawan! A Força é forte em você, continue seu treinamento."
elif 4 <= pontuacao < 7:
    mensagem_final = "Hmm... Treinar mais você precisa. Mas potencial você tem, sim."
elif 1 <= pontuacao < 4:
    mensagem_final = "A Força... não está muito presente aqui. Mas não desista, até o Luke começou do zero!"
else:
    mensagem_final = "Você está mais perdido que stormtrooper atirando! Hora de rever os filmes, padawan."

for letra in mensagem_final:
    print(letra, end='', flush=True)
    time.sleep(0.07)

print("\n")