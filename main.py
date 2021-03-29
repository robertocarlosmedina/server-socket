import pygame
from pygame import *
import os
from serversSockets.tcp import client
from components.colors import color
from textInput import Textinput

keep_going = True


pygame.init()
screen_size = (640, 420)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("ChatBox")

user = client.User()
text = Textinput()

send = False
event = None

while keep_going:
    screen.fill(color.black.value)
    all_event = pygame.event.get()
    for event in all_event:
        if event.type == QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_RETURN]:
                send = True
            elif pygame.key.get_pressed()[K_KP_ENTER]:
                exit()
    t = text.settingInputText(all_event, screen)
    
    if send:
        user.serverConectAndSend(t)
        send = False
    pygame.display.update()
