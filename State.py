state_size = 5


class State:

    def __init__(self, collision_gauche, collision_face, collision_droite, vertical_orientation, horizontal_orientation):
        self.collision_gauche = collision_gauche,
        self.collision_face = collision_face,
        self.collision_droite = collision_droite,
        self.vertical_orientation = vertical_orientation,
        self.horizontal_orientation = horizontal_orientation


    