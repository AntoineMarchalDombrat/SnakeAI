from Agent import Agent
from SnakeGame import SnakeGame, manual_action
from State import State

import pprint

if __name__ == "__main__":
    #lancement de la partie
    game = SnakeGame()
    state = State.stateFromSnake(game)
    agent = Agent()

    while True:

        #Manual action retourne une action en fonction de la touche tapée
        #action = manual_action()

        #automatique
        action = agent.select_action(state)
        reward, game_over, score = game.play_step(action)
        new_state = State.stateFromSnake(game)
        #State.printState(new_state)
        print("state", state)
        print("new_state", new_state)
        agent.update_q_value(state, reward, action, new_state, game_over)



        state = new_state

       # print(f"Score: {score}  Reward: {reward}")
        #afficher état
        #state.printState()




        if game_over:
                print("Game Over! Restarting...")
                game.reset()
                game.idGame = game.idGame + 1

                agent.print_qValues()
                agent.epsilon = agent.epsilon * agent.epsilon_decay_rate

        #Verif de fermeture de l'application
        #check_close_window()