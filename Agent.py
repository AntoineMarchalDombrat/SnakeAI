import numpy as np
from State import state_size

action_size = 3

Q_table = np.zeros((state_size, action_size))
print(Q_table) 


def select_action():
    