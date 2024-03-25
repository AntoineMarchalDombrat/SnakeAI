import random
from SnakeGame import Direction
from State import State

action_size = 3

# nb lignes = nbb etats
# nb colonne = nb action


class Agent:
    def __init__(self):
        self.qValuesTable = dict()
        self.epsilon = 1.0
        self.step_size = 0.3
        self.gamma = 0.9  # discount rate
        self.epsilon_decay_rate = 0.95

        for direction in Direction:
           for foodhoriz in range(3):
               for foodvert in range(3):
                   for leftempty in [True,False]:
                       for frontempty in [True,False]:
                           for rightempty in [True,False]:

                               state1 = State(direction, foodhoriz, foodvert, leftempty, frontempty, rightempty)
                               if state1 not in self.qValuesTable:
                                   # If it doesn't exist, create it and fill it with zeros
                                   self.qValuesTable[state1] = [0,0,0]

    def random_action(self):
        action = random.randint(0, 2)

        return action

    def select_action(self, state):
        if state not in self.qValuesTable:
            self.qValuesTable[state] = [0,0,0]

        rand = random.uniform(0, 1)
        if rand < self.epsilon:
            return self.random_action()

        # tableu des score de chaque action
        q_values = self.qValuesTable[state]
        print("q_values:", q_values)

        # Détermination de l'action avec la valeur Q maximale
        max_q_value = q_values.index(max(q_values))
        # Sélection de toutes les actions ayant la même valeur Q maximale
       # best_actions = [action for action, value in q_values.items() if value == max_q_value]
        #if (len(best_actions) != 1):
            # Choix aléatoire d'une action parmi les meilleures actions
         #   selected_action = random.choice(best_actions)
        return max_q_value
        #return selected_action

    def update_q_value(self, state, reward, action, next_state, done):
        """ Q(s, a) += alpha * (r(s, a) + gamma * max Q(s', .) - Q(s, a)) """
#/!\
        if next_state not in self.qValuesTable:
            self.qValuesTable[next_state] = [0,0,0]
            #print(next_state)
            print("NEVERRRRRRRRRRRRRRRRRRRRRRRRR")
            for i in range(action_size):
                self.qValuesTable[next_state][i] = 0

        max_q_next = max(self.qValuesTable[next_state])
        # max_q_next = max([self.qValuesTable[next_state][a] for a in range(action_size)])
        # no need to include the value of the next state if done
        self.qValuesTable[state][action] =self.qValuesTable[state][action] + self.step_size * (
                reward + self.gamma * max_q_next * (1.0 - done) - self.qValuesTable[state][action])
        if (self.qValuesTable[state][action] != 0.0):
            print("Nouvelle qValue :")
            print(self.qValuesTable[state][action])

    def print_qValues(self):
        """for direction in range(4):
            for foodhoriz in range(3):
                for foodvert in range(3):
                    for leftempty in range(3):
                        for frontempty in range(2):
                            for rightempty in range(2):
                                state1 = State(direction,foodhoriz, foodvert, leftempty,frontempty,rightempty)
                                state1.printState()
                                print(self.qValuesTable[state1])"""


"""
    def act(self, snake, food):
        state = self._GetState(snake, food)
        rand = random.uniform(0, 1)
        if rand < self.epsilon:
            action_key = self.random_action()

        q_values = {a: self.q[state][a] for a in self.actions}
        max_q = max(q_values.values())

        # random sampling for actions that have the same maximum Q value
        actions_with_max_q = [a for a, q in q_values.items() if q == max_q]
        return np.random.choice(actions_with_max_q)

        # Epsilon greedy

        else:
            state_scores = self.qvalues[self._GetStateStr(state)]
            action_key = state_scores.index(max(state_scores))
        action_val = self.actions[action_key]

        # Remember the actions it took at each state
        self.history.append({
            'state': state,
            'action': action_key
        })
        return action_val





"""
