# Neste projeto você desenvolverá o jogo pedra, papel e tesoura. 
# Os jogadores serão o usuário e o computador.
# O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel" ou "tesoura" 
# E então o computador irá fazer a escolha aleatoriamente, após isso,  o jogo deve informar quem venceu. 
# Para recordar:
# Pedra > tesoura 
# Tesoura > Papel 
# Papel > Pedra 
# Utilize funções para separar cada funcionalidade do jogo!

# importar libs
import random
#lista com opções:
options= ["rock","paper", "scissors"]
# Funções com cada opção de escolha
def ChoiceComparisson(user_choice):
    computer_input= random.choice(options)
    if user_choice == "rock" and computer_input=="scissors":
        print("You won!")
    elif user_choice =="scissors" and computer_input == "paper":
        print("You won!")
    elif user_choice =="paper" and computer_input == "rock":
        print("You won!")    
    elif user_choice == computer_input:
        print("It's a tie")
    else:
        print("You lost")
    print(f" User:{user_choice}\n Computer:{computer_input}")

def treatment(input):
    if input== "1":
        return "rock"
    elif input== "2":
        return "paper"
    elif input== "3":
        return "scissors"
    elif type(input) == str:
        return input.lower()
# Mensagem de boas vindas, explicação do jogo e solicitar o input do usuário
print("\n"," Welcome to Rock, paper and scissors game:")
print('''
  Choose an option and try to defeat me !!!
      Remember:
        # Rock > Scissors 
        # Scissors > Paper 
        # Paper > Rock 
''')
user=input(" What is your choice?\n 1.Rock\n 2.Paper\n 3.Scissors\n")
###insert validation here###
user= treatment(user)
# Exibir mensagem de vitória, empate, ou derrota
print("\n ")
ChoiceComparisson(user)