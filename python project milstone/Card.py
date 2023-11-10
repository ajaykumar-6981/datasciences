import random

#suit
suits=('jack','spade','diamond','heart')
#rank
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
#value
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class Card:
     def __init__(self,suit,rank):
          self.suit=suit
          self.rank=rank
          self.value=value[rank]
     def __str__(self):
          return self.rank+" of "+ self.suit

two_hearts=Card("Hearts","Two")

print(two_hearts)
print(two_hearts.suit)
print(two_hearts.rank)

class Deck:
     def __init__(self):
          self.all_cards=[]

          for suit in suits:
               for rank in ranks:
                    created_Card=Card(suit,rank)

                    self.all_cards.append(created_Card)

     def shuffle(self):
          random.shuffle(self.all_cards)

     def deal_one(self):
          return self.all_cards.pop()

new_Deck= Deck()

first_card=new_Deck.all_cards[0]
bottom_card=new_Deck.all_cards[-1]

print(first_card,bottom_card)

new_Deck.shuffle()

print(new_Deck.all_cards[-1])

popped=new_Deck.deal_one()
print(popped)
print(len(new_Deck.all_cards))

class Player:
     def __init__(self,name):
          self.name=name
          self.all_cards=[]

     def remove_one(self):
          return self.all_cards.pop(0)

     def add_card(self,new_cards):
          if(type(new_cards)==type([])):
               #list fo multiple cards
               self.all_cards.extend(new_cards)
          else:
               #for single card
               self.all_cards.append(new_cards)
     def __str__(self):
          return f'Player {self.name} has {len(self.all_cards)} cards'


newPlayer=Player("Ajay")

mycard=Card("King","Four")
newPlayer.add_card(mycard)

print(newPlayer.all_cards[0])

newPlayer.add_card([mycard,mycard,mycard])
print(newPlayer)

newPlayer.remove_one()
print(newPlayer)

# Game Setup
player_one=Player("One")
player_two=Player("Two")

new_deck=Deck()
new_deck.shuffle()

# half of 52 deck card
for x in range(26):
     player_one.add_card(new_deck.deal_one())
     player_two.add_card(new_deck.deal_one())

# print(player_one.all_cards(0))

#while game_on
game_on=True

round_num=1
# while(game_on):

while game_on:
     round_num +=1
     print(f"Round{round_num}")

     if len(player_one.all_cards)==0:
           print('Player One,out of cards! Player Two Wins !')
           game_on =False
           break
     if len(player_two.all_cards)==0:
           print('Player Two,out of cards! Player  One Wins !')
           game_on=False
           break

     #START A NEW ROUND
     player_one_cards=[]
     player_one_cards.append(player_one.remove_one())
     player_two_cards=[]
     player_two_cards.append(player_two.remove_one())

     at_war= True

     while at_war:
          if player_one_cards[-1].value>player_two_cards[-1].value:
               player_one.add_card(player_one_cards)
               player_one.add_card(player_two_cards)

               at_war=False
          elif player_one_cards[-1].value<player_two_cards[-1].value:
               player_two.add_card(player_one_cards)
               player_two.add_card(player_two_cards)

               at_war=False
          else:
               print('WAR!')

               if len(player_one.all_cards)<3:
                    print("Player One Unable to declare war")
                    print("Player Two Wins1")
                    game_on=False
                    break

               if len(player_two.all_cards) < 3:
                    print("Player One Unable to declare war")
                    print("Player One Wins1")
                    game_on = False
                    break

               else:
                    for num in range(3):
                         player_one_cards.append(player_one.remove_one())
                         player_two_cards.append(player_two.remove_one())


