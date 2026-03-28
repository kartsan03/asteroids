import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

	def __init__ (self, position, radius):
		super().__init__(position.x, position.y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius)

	def update(self, dt):
		self.position += dt * self.velocity
