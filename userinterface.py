

from base import Base
import tkinter as tk
import pygame
import sys

def run_program():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    
    b = Base(60, 30, 100, False, 'Lopro', 5)
    
    
    while True:
        
        
        #constantly check for new events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((230,230,230))        
        pygame.draw.rect(screen, (0,0,0),(600, 400, b.length*2, b.width*2), b.value)
        pygame.draw.rect(screen, (70,70,70),(150,450,100,50))
        
        pygame.display.flip()
        
run_program();


