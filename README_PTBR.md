# Jogo pedra-papel-tesoura

:fist_raised: :raised_hand_with_fingers_splayed: :v:

## Descrição

Esse é um projeto de um jogo pedra-papel-tesoura criado em python, ele se baseia em um desafio proposto nas aulas de programação Full Stack da Infinity school visual art center.  
A aplicação consiste em um jogo simples onde o usuário escolhe uma opção e recebe a mensagem informando que venceu, perdeu ou empatou.  
Inicialmente o programa usa somente python para criação do código, porém também foram adicionados as bibliotecas random para realizar uma escolha aleatória por parte do computador e tkinter para criar uma interface gráfica simples.  
Após a criação do programa, pretendo colocá-lo em uma interface gráfica e finalmente criar um website ou transformá-lo em executável para que os usuários possam acessar o conteúdo.
Fico feliz por conseguir finalizar esse projeto em apenas 1 dias  

## Como usar o projeto

(inserir instruções)

## Logica de programação e fluxograma:

1. importar libs.  
2. Funções com cada opção de escolha.  
    2.1. Imprimir o resultado dependendo da condição.
        - Caso usuário escolha uma opção que vença computador, imprimir mensagem ***"You won!"***  
        - Caso usuário escolha uma opção igual ao computador, imprmir mensagem   ***"It's a tie!"***   
        - Caso usuário escolha uma opção que perca, imprimir mensagem ***"You lost!"***  
3. Exibir mensagem de boas vindas e  explicação do jogo  
4. Solicitar a escolha do usuário.    
    4.1. Validar e Tratar da escolha do usuário.  
5. Exibir mensagem de vitória, empate, ou derrota e escolhas do usuário e computador

6. (passo extra) Adicionar uma interface de usuário para o jogo.

<br>
<br> 
<br>
<br>        
<img src="https://hips.hearstapps.com/hmg-prod/images/people-playing-paper-rock-scissors-royalty-free-illustration-1583269312.jpg" alt="Rock, paper and scissors" width="500"/>



## Desafios encontrados:
1.Primeiro desafio encontrado foi na transição de um programa somente em linha de comando no terminal para um programa com interface, anteriormente eu havia criado uma função única para checar a escolha do usuário e retornar o resultado em comparação com a escolha da máquina. Agora precisei separar em 3 funções distintas, cada uma com processos separados.   
2. Outro desafio foi colocar uma imagem em um botão para servir de referência ao usuário. Tive que importar uma segunda biblioteca para tratamento de imagens: a PLI.   

## referências:
1. https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/  
2. https://docs.python.org/3/library/tkinter.html

> [!TIP]
> Lembre-se de colocar uma estrela nesse repositório !!!
