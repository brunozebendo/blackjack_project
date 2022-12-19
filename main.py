############## Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear

def deal_cards():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card
'''uma função só pode ser chamada, depois de criada, por isso a função deal_cards foi removida para o começo
 do código'''
"""importou a função random que escolhe randomicamente, criou-se a lista cards e chamou a função interna 
random e guardou dentro de uma variável chamada card, ou seja, dentro de uma lista de cartas,
 selecionou-se uma escolhida randomicamente e o return marca o fim da função"""
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_scores(cards):
#if 11 in cards and 10 in cards and len(cards)==2:
if sum(cards) == 21 and len(cards)==2:
return 0
return sum(cards)
if 11 in cards and sum(cards) > 21:
cards.remove(11)
cards.append(1)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21,
# then the user loses. If the computer_score is over 21, then the computer loses. If none of the above,
# then the player with the highest score wins.
def compare(user_score, computer_score):
	if user_score == computer_score:
	return "it's a draw"
	elif computer_score == 0:
	return "you lose, opponent has a blackjack"
	elif user_score == 0:
	return "Win with a Blackjack"
	elif user_score > 21:
	return "You went Over"
	elif computer_score > 21:
	return "Opponent went over, you win"
	elif user_score > computer_score:
	return "You win"
	else:
	return "You lose"
'''aqui se cobriu todas as opções de resultado dentro de uma função e no final do código se chamou essa função'''
def play_game():
	user_cards = []
	computer_cards = []
	for _ in range(2):
		user_cards.append(deal_cards())
		computer_cards.append(deal_cards())
		calculate_scores(user_cards)
	new_card = deal_cards() user_cards.append(new_card)
"""Criou a variável em uma lista vazia para o usuário e para o computador e depois, para criar duas cartas,
 usa-se a função range que vai iterar pela função deal_cards, que foi passado como atributo,
  usou-se o _ pois esse item não vai ser reusado, então guardou-se o resultado dentro da variável new_card,
   então usa-se a função append para incluir a nova carta ao user_cards, 
   não se pode usar a função += ou a função extend(que são a mesma coisa), pois elas só funcionam para listas,
    quando se quer acrescentar um item apenas, se usa append.
     Após fazer esse primeiro código (que deixei comentado), ele foi refatorado em um mais simples
     que faz a mesma função"""
#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
"""criou-se a função e passou como parâmetro a lista de cards, a função irá executar a função sum
 que soma todos os itens de uma lista da esquerda para a direita"""
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
# instead of the actual score. 0 will represent a blackjack in our game.
''' em uma linha de código definiu-se a regra para verificar se aconteceu um blackjack,
 que é verificar se tem apenas duas cartas, uma delas sendo o ás que vale 11 e a outra uma que valha 10,
  depois comentei o código que foi refatorado para apenas somar as cartas e verificar se a soma é 21'''
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11
# and replace it with a 1. You might need to look up append() and remove().
"""definiu-se a a regra da dica 8, se o ás, que vale 11, estiver presente em cards e a soma for maior
 que 21, então ele remove o 11 e o substitui por 1, que também é o ás. A função remove busca a primeira
  correspondência do item passado como parâmetro na lista e o append acrescenta o parâmetro no final da lista"""
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score
# is over 21, then the game ends.
is_game_over = False
while not is_game_over:
user_score = calculate_scores(user_cards)
computer_score = calculate_scores(computer_cards)
print(f" Your cards {user_cards}, current_scores {user_score}")
print(f" Computers first card {computer_cards[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
is_game_over = True
else:
user_should_deal = input("type 'y' to get another card or type 'n' to pass:")
if user_should_deal =="y" :
user_cards.append(deal_cards())
else:
is_game_over = True
""" chamou-se a função calculate_scores, guardou em uma variável e passou o parâmetro das cartas de cada um,
 ou seja, a função vai verificar o deck de cada usuário e calcular se não ocorreu um blackjack,
  em uma linha determinou a regra de verificação do blackjack, essa regra na função calculate_scores,
   então criou-se a variável is_game_true, para depois usá-la para determinar o fim do jogo.
    aqui é a verificação do hint 10, criou uma variável para dentro do input determinar se o usuário
     quer continuar ou não, caso sim, vai acrescentar (append) mais uma carta, através da função deal_cards"""
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use
# the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need
# to be repeated until the game ends.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing
# cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
computer_cards.append(deal_cards())
computer_score = calculate_scores(computer_cards)
print(f" Your final hand: {user_cards}, final score {user_score}")
print(f" Computer final hand: { computer_cards}, final score {computer_score}")
print(compare(user_score, computer_score))
'''O código diz que se a pontuação do computador for diferente de zero (que é atingido no blackjack)
 e for menor que 17, deve-se acrescentar uma carta através da função deal cards e a nova pontuação
  vai ser acionada pela função calculate passando como parâmetro as cartas do computador.'''
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and
# start a new game of blackjack and show the logo from art.py.
while input("Do you wanna play some Blackjack? Type 'y' or 'n'") == "y":
clear()
play_game()
'''quando o input vem isolado, ele vai ser inteiramente substituído’'''