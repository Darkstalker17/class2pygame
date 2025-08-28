import pygame
pygame.init()
window = pygame.display.set_mode((1200, 900))
'''
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))    
  
    pygame.display.flip()
window.fill((255, 255, 255))
GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
pygame.display.update()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()'''

import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')
    colors = {'red': pygame.Color('red'),
              'green': pygame.Color('green'),
              'blue': pygame.Color('blue'),
              'yellow': pygame.Color('yellow'),
              'white': pygame.Color('white'),
              }
    current_color = colors['white']
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()

    