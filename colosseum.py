#from netlearner import DQNLearner
import numpy as np


#card types as classes
import itertools
from random import choice
from random import shuffle, randint

rl_model_name = '9_18_run_4'

card_deck = ['quick','quick','quick',
             'arts','arts','arts','arts','arts','arts',
            'buster','buster','buster','buster','buster','buster']
hp = 30

class team_chaldela:
    #hp is total team hitpoints
    #deck is the total 15 card deck of the team
    
    def __init__(self):
        self.hit_points = hp
        self.card_deck = card_deck
        self.np_charge = 0
        self.current_stars = 0

    def get_action(self, state =None):
        print('hi')

class enemy_servants:
    
    def __init__(self,hp):
        self.hit_points = hp
        


def deal_hand(deck):
    shuffle(deck)
    
    return deck[:5] 

class Buster:
    def __init__(self, card_number):
        if card_number == 1:
            self.dmg = 1.5
            self.np_gain = 0
            self.stars = 1
            
        if card_number == 2:
            self.dmg = 1.8
            self.np_gain = 0
            self.stars = 2
            
        if card_number == 3:
            self.dmg = 2.1
            self.np_gain = 0
            self.stars = 3
            
class Arts:
    def __init__(self, card_number):
        if card_number == 1:
            self.dmg = 1.0
            self.np_gain = 4
            self.stars = 0
            
        if card_number == 2:
            self.dmg = 1.2
            self.np_gain = 5
            self.stars = 0
            
        if card_number == 3:
            self.dmg = 1.4
            self.np_gain = 6
            self.stars = 0
            
class Quick:
    def __init__(self, card_number):
        if card_number == 1:
            self.dmg = .8
            self.np_gain = 2
            self.stars = 4
            
        if card_number == 2:
            self.dmg = 0.96
            self.np_gain = 3
            self.stars = 6
            
        if card_number == 3:
            self.dmg = 1.12
            self.np_gain = 4
            self.stars = 8
            
#using the input list which is just a list of strings of card types
# convert them into card objects which have stats and such
def command_card_gen(card_type,current_card_num):
    
    if card_type == 'buster':
        card = Buster(current_card_num)
    elif card_type == 'arts':
        card = Arts(current_card_num)
    elif card_type == 'quick':
        card = Quick(current_card_num)
    return card

#there is a bonus that gets applied based on the first card. 
# so check the first card and then we can apply the modifiers 
# in the rest of the cards
def first_card_mods(first_card):
    
    if first_card == 'buster':
        dmg_modifier = 1.5
        np_mod = 1.0
        star_mod = 1
        
    elif first_card == 'arts':
        dmg_modifier = 1.0
        np_mod = 2.0
        star_mod = 1
        
    elif first_card == 'quick':
        dmg_modifier = 1.0
        np_mod = 1.0
        star_mod = 1.2
    else:
        print('invalid command card')
    return dmg_modifier,np_mod,star_mod

#since card chains of 3 have a bonus, this function can be 
# used to apply them... work in progress
def card_chain_effect(cards_to_play,team_obj,round_reward):
    #print(cards_to_play)
    #takes command card chain (list), checks for chain, applies bonuses
    buster_chain_mod = 1
    
    if cards_to_play.count('buster') == 3:
        #print('buster chain!')
        buster_chain_mod = 1.2
        round_reward+=2
        #print('')
    elif cards_to_play.count('arts') == 3:
        team_obj.np_charge +=20
        round_reward+=2
        #print('Arts chain!')
        #print('')
    elif cards_to_play.count('quick') == 3:
        team_obj.current_stars +=10
        round_reward+=2
        #print('quick chain!')
        #print('')
    else:
        #print('')
        #print('not a chain')
        buster_chain_mod = 1
    return buster_chain_mod, round_reward

def critical_role(team_obj):
    critical_chance = team_obj.current_stars*2
    critical_flip = randint(1,100)
    if critical_flip <=critical_chance:
        critical_mod = 2.0
        #print('')
        #print('NATURAL 20 MOTHERFUCKKAAA')
    else:
        critical_mod = 1.0
    
    team_obj.current_stars = 0
    return critical_mod
    
# combine the previous functions to calculate the damage output and whatnot 
# of a single chain
def use_NP(team_obj,total_damage):
    if team_obj.np_charge >= 100:
        total_damage += 20
        #print('')
        #print('USED NP')
        #print('')
        team_obj.np_charge = 0
    return total_damage
    
def calc_chain_damage(team_obj, card_chain, round_reward):
    total_damage = 0
    first_card = card_chain[0]
    #print(first_card)
    dmg_modifier, np_mod, star_mod = first_card_mods(first_card)
    crit_mod = critical_role(team_obj)
    
    #using the NP should occur before card chain effects are calculated
    total_damage = use_NP(team_obj,total_damage)
    #arts and quick chain bonuses are executed in the 
    # card chain effect function
    #adding buster effect into the damage calculation    
    buster_chain_effect, round_reward = card_chain_effect(card_chain,team_obj,round_reward)
    
    for i in range(3):
        card = command_card_gen(card_chain[i],i+1)
        #star generation
        card_stars = card.stars*star_mod
        team_obj.current_stars += card_stars
        
        #dmg 
        
        card_dmg = card.dmg *dmg_modifier *buster_chain_effect*crit_mod
        total_damage+= card_dmg
        
        #np
        card_np_gain = card.np_gain*np_mod
        team_obj.np_charge += card_np_gain
    if team_obj.np_charge >= 100:
        round_reward +=1

    return total_damage, round_reward

#will need to adjust? to make it match the keras input
def pick_cards(current_hand5,card_indexes = [0,1,2]):
    #cards can take on values of 0-4 and should be a list of ints
    #default is first 3 cards
    hand_to_play = []
    for i in card_indexes:
        hand_to_play.append(current_hand5[i])
    
    return hand_to_play
    
def random_pick_cards():
    list1= list(itertools.permutations([0,1,2,3,4],3))
    hand = choice(list1)
    return hand 
# fight till one team drops.     

def check_if_alive(team_instance):
    #if team's hp is higher than 0 than return true, 
    # false when one player drops to 0 or below
    if team_instance.hit_points >0:
        return 'alive'
    else:
        return 'dead'


class Battle:
    
    def __init__(self, num_learning_rounds =None, learner = None, report_every=10000):
        self._num_learning_rounds = num_learning_rounds
        self._report_every = report_every
        self.player = learner
        self.win = 0
        self.loss = 0
        self.game = 1
        self.evaluation = False
        
    def fight_battle(self):
        turn = 0
        
        player_team, enemy_team = self.reset_battle()
        
        while True:
            round_reward = 0 
            turn+=1
            enemy_dps = randint(1,3)

            if self.evaluation == True:
                print('Evaluation Round')
                print('turn: ',turn)
            
            #### PLAYER TURN SECTION
            current_hand = deal_hand(player_team.card_deck)
            if self.evaluation ==True:
                print('hand is: ',current_hand)
            #send list to the model
            p1_action = player_team.get_action(current_hand) #comment out for auto testing
            #p1_action = random_pick_cards() #testing pipeline
            
            #it should return an iterable? i think a tuple? of length 3 which correspond
            # to the card indicies
            
            #3 card tuple fed into pick_cards function which will generate the hand and start
            #dmg calculations
            picked_cards = pick_cards(current_hand,p1_action) #
            
            if self.evaluation == True:
                print('cards to play: ',picked_cards, 'indexes: ', p1_action)

            team_dps, round_reward = calc_chain_damage(player_team,picked_cards,round_reward)    

            if self.evaluation == True:
                print('team deals ',team_dps, ' current np bar: ',player_team.np_charge,player_team.current_stars)
                print('enemy deals ',enemy_dps)

            player_team.hit_points -= enemy_dps
            enemy_team.hit_points -= team_dps
            
            #check if player is still alive
            if check_if_alive(player_team) =='alive' and check_if_alive(enemy_team) == 'dead':
                winner = 'player'
                self.win +=1
                round_reward+=1
                if self.evaluation == False:
                    player_team.update(current_hand,round_reward)

                break
                
            elif check_if_alive(player_team) =='dead':
                winner = 'enemy'
                self.loss +=1
                round_reward= -2
                if self.evaluation == False:
                    player_team.update(current_hand,round_reward)
                break
                                  
                # if neither of the states trigger... ie everyone is alive. Then sents an update
                                  # with 0 reward just showing the current hand
            if self.evaluation == False:
                    round_reward+=0
                    player_team.update(current_hand,round_reward)

        if self.evaluation == False:
            self.game += 1
            #print(self.game)
        
        if self.evaluation == True:
            print('')
            print('team_hp: ',player_team.hit_points)
            print('enemy_hp: ',enemy_team.hit_points)
        
        
        #if self.game % 50 ==0:
        #    print('currently on game numnber: ',self.game)
        if self.evaluation == False: 
            self.report(current_hand = current_hand,picked_cards = picked_cards,p1_action = p1_action)

        if self.game == self._num_learning_rounds:
            print("Turning off learning!")
            self.player._learning = False
            self.win = 0
            self.loss = 0

        #epsilon increase overtime starts at 85 for more exploration
        #if self.game==20000:
        #    self.player._epsilon =.9
        #if self.game==40000:
        #    self.player._epsilon =.95
        #if self.game==80000:
        #     self.player._epsilon =.97
        #if self.game==100000:
        #    self.player._epsilon =.99
        #                      
    def reset_battle(self):

        
        team = self.player
        team.hit_points = hp
        team.np_charge = 0
        team.current_stars = 0
        enemy = enemy_servants(110) 
        return team, enemy
    
    def report(self,current_hand,picked_cards,p1_action):
        #turned off for plotting 9/18
        if self.game % self._num_learning_rounds == 0:
            print('##############################################')
            print('#                 Final Score                #')
            print('##############################################')
            print('')
            rint(str(self.game) +","  +str(self.win / (self.win + self.loss)))
            print('')
            print('cards to play: ',current_hand,picked_cards, 'indexes: ', p1_action)
            print('##############################################')
            
            turning off this section for testing
            self.evaluation = True
            self.fight_battle()
            self.evaluation = False
            
            self.win = 0
            self.loss = 0
            self.player.save_rl_model('models/{}_iteration_{}'.format(rl_model_name,self.game))
            
        elif self.game % self._report_every == 0:
            print('##############################################')
            print('#                Updated Score               #')
            print('##############################################')
            print('')
            print(str(self.game) +","  +str(self.win / (self.win + self.loss)))
            print('')
            print('cards to play: ',current_hand,picked_cards, 'indexes: ', p1_action)
            print('##############################################')
            
            turning off this section for testing
            self.evaluation = True
            self.fight_battle()
            self.evaluation = False
            
            self.win = 0
            self.loss = 0
            if self.game % 10000 == 0:
                self.player.save_rl_model('models/{}_iteration_{}'.format(rl_model_name,self.game))
