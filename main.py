import pygame
import sys
from settings import *
from car import Car

# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
car = Car(SC_WIDTH//2, SC_HEIGHT//2,"car.png")

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    car.update()

    #пересечение объектов, collisions
                
    # обновление экрана
    screen.fill(BLACK)
    car.draw(screen)
    pygame.display.update()



    
