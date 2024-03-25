from SnakeGame import Point, BLOCK_SIZE, Direction

state_size = 5


class State:
    def __init__(self, direction, horizontal_orientation, vertical_orientation, left_square_empty, front_square_empty,
                 right_square_empty):
        self.direction = direction
        self.horizontal_orientation = horizontal_orientation
        self.vertical_orientation = vertical_orientation
        self.left_square_empty = left_square_empty
        self.front_square_empty = front_square_empty
        self.right_square_empty = right_square_empty

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return (self.direction, self.horizontal_orientation, self.vertical_orientation, self.left_square_empty, self.front_square_empty, self.right_square_empty) == \
            (other.direction, other.horizontal_orientation, other.vertical_orientation, other.left_square_empty, other.front_square_empty, other.right_square_empty)

    def __hash__(self) -> int:
        # Utilisation d'un tuple des attributs comme clé de hachage
        return hash((self.direction, self.horizontal_orientation, self.vertical_orientation, self.left_square_empty, self.front_square_empty, self.right_square_empty))

    def __str__(self):
        return f"Direction: {self.direction}, Food Horizontal: {self.horizontal_orientation}, Food Vertical: {self.vertical_orientation}, Left Empty: {self.left_square_empty}, Front Empty: {self.front_square_empty}, Right Empty: {self.right_square_empty}"

    def printState(self):
        print("=========================================================================================")
        print("Pomme gauche/pareil/droite : " + str(self.horizontal_orientation))
        print("Pomme haut/pareil/bas : " + str(self.vertical_orientation))
        print("Vide à gauche? : " + str(self.left_square_empty))
        print("Vide en face? : " + str(self.front_square_empty))
        print("Vide à droite? :  " + str(self.right_square_empty))
        print("=========================================================================================")

    @staticmethod
    def stateFromSnake(SnakeG):
        # Détermination de l'orientation horizontale
        if SnakeG.head.x < SnakeG.food.x:
            horizontal_orientation = 0  # Position relative : à gauche
        elif SnakeG.head.x == SnakeG.food.x:
            horizontal_orientation = 1  # Position relative : centré
        else:
            horizontal_orientation = 2  # Position relative : à droite

        # Détermination de l'orientation verticale
        if SnakeG.head.y < SnakeG.food.y:
            vertical_orientation = 0  # Position relative : en haut
        elif SnakeG.head.y == SnakeG.food.y:
            vertical_orientation = 1  # Position relative : centré
        else:
            vertical_orientation = 2  # Position relative : en bas

        # Vérification des cases adjacentes en fonction de la direction du serpent
        if SnakeG.direction == Direction.RIGHT:
            left_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y - BLOCK_SIZE))
            front_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x + BLOCK_SIZE, SnakeG.head.y))
            right_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y + BLOCK_SIZE))
        elif SnakeG.direction == Direction.LEFT:
            left_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y + BLOCK_SIZE))
            front_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x - BLOCK_SIZE, SnakeG.head.y))
            right_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y - BLOCK_SIZE))
        elif SnakeG.direction == Direction.UP:
            left_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x - BLOCK_SIZE, SnakeG.head.y))
            front_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y - BLOCK_SIZE))
            right_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x + BLOCK_SIZE, SnakeG.head.y))
        elif SnakeG.direction == Direction.DOWN:
            left_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x + BLOCK_SIZE, SnakeG.head.y))
            front_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x, SnakeG.head.y + BLOCK_SIZE))
            right_square_empty = not SnakeG.is_collision(Point(SnakeG.head.x - BLOCK_SIZE, SnakeG.head.y))

        return State(SnakeG.direction, horizontal_orientation, vertical_orientation, left_square_empty, front_square_empty,
                     right_square_empty)
