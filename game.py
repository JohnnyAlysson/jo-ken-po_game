# Neste projeto você desenvolverá o jogo pedra, papel e tesoura. 
# Os jogadores serão o usuário e o computador.
# O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel" ou "tesoura" 
# E então o computador irá fazer a escolha aleatoriamente, após isso,  o jogo deve informar quem venceu. 
# Para recordar:
# Pedra > tesoura 
# Tesoura > Papel 
# Papel > Pedra 
# Utilize funções para separar cada funcionalidade do jogo!

# importar libs e assets
import random
from tkinter import *
# from PIL import Image , ImageTk

#lista com opções:
options= ["rock","paper", "scissors"]
# criar funções para cada escolha do usuário
def rock():
    computer_input = random.choice(options)
    if computer_input == "scissors":
        result["text"] ="You won!"
    elif computer_input == "paper":
        result["text"] = "You lost!"
    else:
        result["text"] ="It's a tie"
    show_user_choice["text"] = "rock"
    show_computer_choice["text"]= computer_input

def paper():
    computer_input=random.choice(options)
    if computer_input == "rock":
        result["text"] = "You won!"
    elif computer_input == "scissors":
        result["text"] = "You lost!"
    else:
        result["text"] = "It's a tie"
    show_user_choice["text"] = "paper"
    show_computer_choice["text"]= computer_input
def scissors():
    computer_input=random.choice(options)
    if computer_input== "paper":
        result["text"] = "You won!"
    elif computer_input=="rock":
        result["text"] = "You lost!"
    else:
        result["text"] = "It's a tie"
    show_user_choice["text"] = "scissors"
    show_computer_choice["text"]= computer_input

# Mensagem de boas vindas, explicação do jogo e solicitar o input do usuário
# Exibir mensagem de vitória, empate, ou derrota
print("\n ")
window = Tk()
rock_img= PhotoImage(file="./assets/rock.png")
img_rock= rock_img.subsample(3,3)
paper_img= PhotoImage(file="./assets/paper.png")
img_paper= paper_img.subsample(2,2)
scissors_img= PhotoImage(file="./assets/scissors.png")
img_scissors= scissors_img.subsample(3,3)
window.title("Rock, paper or Scissors")
welcome_text = Label(window, text=" Choose an option and try to defeat me !!!")
welcome_text.grid(column=1, row=0)
intructions= Label(window, text='''
      Remember:
        # Rock > Scissors 
        # Scissors > Paper 
        # Paper > Rock ''' )
intructions.grid(column=1, row=1)

button_rock= Button(window,image=img_rock,command=rock,)
button_rock.grid(column=0,row=2)
button_paper= Button(window,image=img_paper,command=paper,)
button_paper.grid(column=1,row=2)
button_scissors= Button(window,image=img_scissors,command=scissors,)
button_scissors.grid(column=2,row=2)

user_text =Label(window,text="Your choice:")
user_text.grid(column=0,row=3)
computer_text=Label(window,text="Computer choice:")
computer_text.grid(column=2,row=3)
show_user_choice = Label(window,text="")
show_user_choice.grid(column=0,row=4)
show_computer_choice = Label(window,text="")
show_computer_choice.grid(column=2,row=4)

result = Label(window,text="")
result.grid(column=1,row=5)
window.mainloop()