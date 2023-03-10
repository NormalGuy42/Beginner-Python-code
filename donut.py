import pygame
import math
import colorsys, random

pygame.init()

#color variables
white = (255,255,255)
black = (0,0,0)
hue = 0

#screen variables
#Screen size
width = 800
height = 720

#Donut positions and size
x_start,y_start = 0,0
x_separator = 10
y_separator = 20

rows = height// y_separator
columns = width // x_separator

screen_size = rows * columns

x_offset = columns/2
y_offset = rows /2

#Donut variables
A,B = 0,0 #rotation animation
theta_spacing = 10
phi_spacing = 2 #increase to increase rotation speed

chars = ".,-~:;=!*#$@" #luminance index

screen = pygame.display.set_mode((width,height))
display_surface = pygame.display.set_mode((width,height))
#display_surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Donut')

font = pygame.font.SysFont('Arial',18, bold=True)
def rgbStuff(r,g,b):
    return tuple(round(i*255) for i in colorsys.hsv_to_rgb(r,g,b))

def text_display(letter, x_start,y_start):
    text = font.render(str(letter),True, rgbStuff(hue, 1, 1))
    display_surface.blit(text,(x_start,y_start))

def text_display_white(letter, x_start,y_start):
    text = font.render(str(letter),True, white)
    display_surface.blit(text,(x_start,y_start))

run = True
while run:
    screen.fill(black)
    z = [0] * screen_size #Fills donut
    b = [' '] * screen_size #Fills empty space for Background


    #Donut Shape logic
    for j in range(0,628, theta_spacing):
        for i in range(0,628,phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1/ (c * h * e + f * g +5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t *n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n ))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    
   # def color_change():
   #     color = text_display(b[i], x_start,y_start)
   #Donut spin logic
    if y_start == rows * y_separator - y_separator:
        y_start = 0
    for i in range(len(b)):
        A += 0.00002 #increase A,B for faster rotation
        B += 0.00001
        color = text_display_white(b[i], x_start,y_start)
        #for event in pygame.event.get():
         #   if event.type == pygame.KEYDOWN:
          #      if event.key == pygame.K_c:
           #         color = color = text_display(b[i], x_start,y_start)
        if i == 0 or i % columns:
            color
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            color
            x_start += x_separator
    
   

    pygame.display.update()
    hue += 0.005

    #Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        
