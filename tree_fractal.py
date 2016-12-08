import pygame, math
pygame.init()

surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.29
   trunk_length = sz * trunk_ratio
   delta_x = trunk_length * math.cos(heading)
   delta_y = trunk_length * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)
# pygame.draw.circle(main_surface, color, (int(posn[0]), int(posn[1])), 3)
# uncoment to draw circles at the ends^

   if order > 0:   # Draw another layer of subtrees

      # Changes the colors of the two fractal trees and allows to change
      # if depth is even or odd or etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
          color1 = color
          color2 = color

      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1)
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1)

def gameloop():

    theta = 0
    while True: # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        theta += 0.01

        main_surface.fill((255, 255, 0)) #change background color
        draw_tree(9, theta, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)
        pygame.display.flip()
        my_clock.tick(120)


gameloop()
pygame.quit()
