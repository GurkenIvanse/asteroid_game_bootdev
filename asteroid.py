from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface ,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position = self.position + self.velocity*dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            asteroid_one = self.velocity.rotate(angle)
            asteroid_two = self.velocity.rotate(-angle)

            new_radius = self.radius-ASTEROID_MIN_RADIUS

            one = Asteroid(self.position.x, self.position.y, new_radius)
            two = Asteroid(self.position.x, self.position.y, new_radius)

            one.velocity = 1.2 * asteroid_one
            two.velocity = 1.2 * asteroid_two
    