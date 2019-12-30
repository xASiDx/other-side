import random

#game menu
choise_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "exit"
}
#possible game results
game_results = {
    1: "\nDang it! You loose...",
    2: "\nHooray! You win!",
    3: "\nIt's a draw."
}

def choise(options):
    incorrect_input = True
    while incorrect_input:
        player_input = input("Please choose:\n 1 for {0},\n 2 for \
{1},\n 3 for {2},\n 4 to {3} the game\n".format(options[1],options[2],options[3],options[4]))
        if player_input.isdigit() and int(player_input) in options:
            incorrect_input = False
        else:
            print("\nIncorrect Input! Please enter numbers 1 - 4")
    return options[int(player_input)]

#variables to keep score
player_score = 0
npc_score = 0
#the functions checks player's and npc's choises and returns corresponding game result
#when player wins we increment his win counter, and vice versa with npc
def check(player_choise, npc_choise, player_win, npc_win):
    if player_choise == "exit":
        return 0
    elif player_choise == "rock":
        if npc_choise == "rock":
            return (3, player_win, npc_win)
        elif npc_choise == "paper":
            npc_win += 1
            return  (1, player_win, npc_win)
        else:
            player_win += 1
            return (2, player_win, npc_win)
    elif player_choise == "paper":
        if npc_choise == "paper":
            return (3, player_win, npc_win)
        elif npc_choise == "scissors":
            npc_win += 1
            return (1, player_win, npc_win)
        else:
            player_win += 1
            return (2, player_win, npc_win)
    else:
        if npc_choise == "scissors":
            return (3, player_win, npc_win)
        elif npc_choise == "rock":
            npc_win += 1
            return (1, player_win, npc_win)
        else:
            player_win += 1
            return (2, player_win, npc_win)

#setting game result to not zero to start the game
game_result = 1
while game_result:
    print("\n\nLet's play Rock, Paper, Scissors!")
    #player chooses
    player_choise = choise(choise_options)
    #npc is assigned with random choise
    npc_choise = choise_options[random.randint(1,3)]
    #checking who's won
    game_result = check(player_choise, npc_choise, player_score, npc_score)
    #and inform player about it
    if game_result:
        player_score = game_result[1]
        npc_score = game_result[2]
        print("Your apponent chooses", npc_choise, game_results[game_result[0]])
#leaving the game
print("\nTotal score:\nYou won - {0}\nYou lost - {1}\n".format(player_score, npc_score))
print("Thanks! Bye!")
input("Press Enter to close the window")
