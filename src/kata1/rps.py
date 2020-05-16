from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if(player == ai):
        return "Empate!"

    if(options[player] == "Piedra" and options[ai] == "Papel"):
        return "Perdiste!"
    if(options[player] == "Papel" and options[ai] == "Tijeras"):
        return "Perdiste!"
    if(options[player] == "Tijeras" and options[ai] == "Piedra"):
        return "Perdiste!"
    if(options[player] == "Piedra" and options[ai] == "Tijeras"):
        return "Ganaste!"
    if(options[player] == "Papel" and options[ai] == "Piedra"):
        return "Ganaste!"
    if(options[player] == "Tijeras" and options[ai] == "Papel"):
        return "Ganaste!"

# Entry Point
def Game():

    player = randint(0, 2)
    ai = randint(0, 2)
    
    winner = quienGana(player, ai)

    print(winner)


# Start game
Game()
