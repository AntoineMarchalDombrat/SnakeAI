import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.SysFont('arial', 25)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point', 'x, y')

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 100  # Ajustez la vitesse du serpent selon vos préférences


class SnakeGame:
    def __init__(self, w=640, h=480):
        self.idGame = 0

        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    # Renvoie vrai si

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        textidgame = font.render("N° "+ str(self.idGame),True,WHITE)
        self.display.blit(text, [0, 0])
        self.display.blit(textidgame, [0,30])
        pygame.display.flip()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def play_step(self, action):
        self.frame_iteration += 1
        old_dist_x = abs(self.head.x - self.food.x)
        old_dist_y = abs(self.head.y - self.food.y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self._move(action)
        self.snake.insert(0, self.head)
        reward = 0
        game_over = False
        new_dist_x = abs(self.head.x - self.food.x)
        new_dist_y = abs(self.head.y - self.food.y)
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
        elif self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()

        else :
            self.snake.pop()
            if new_dist_x < old_dist_x or new_dist_y < old_dist_y:
                reward = 1


        self._update_ui()
        self.clock.tick(SPEED)
        return reward, game_over, self.score

    def _move(self, action):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)
        if action == 0:  # Tout droit
            new_dir = clock_wise[idx]
        elif action == 1:  # Tourner à droite
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]
        else:  # [0, 0, 1] c'est-à-dire tourner à gauche
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]
        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)


def manual_action():
    keys = pygame.key.get_pressed()
    # par défaut
    action = [1, 0, 0]
    if keys[pygame.K_UP]:
        action = [0, 0, 1]  # Tourner à gauche
    elif keys[pygame.K_DOWN]:
        action = [0, 1, 0]  # Tourner à droite
    elif keys[pygame.K_LEFT]:
        action = [1, 0, 0]  # Tout droit
    return action


def check_close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
