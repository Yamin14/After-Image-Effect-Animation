import pygame
pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
cyan = (0, 255, 255)
yellow = (255, 255, 0)

x, y = [100]*5, [150, 300, 450, 600, 750]
col = [magenta, blue, green, orange, red]
speed = [20, 40, 60, 80, 100]
direction = [1]*5

while running:
	screen.fill(yellow)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	for i in range(5):
		pygame.draw.circle(screen, col[i], (x[i], y[i]), 50)
	
		if direction[i] == 1:
			x[i] += speed[i]
		elif direction[i] == -1:
			x[i] -= speed[i]

		if x[i] >= 700:
			direction[i] = -1
		if x[i] <= 0:
			direction[i] = 1
		
	pygame.display.flip()

pygame.quit()
