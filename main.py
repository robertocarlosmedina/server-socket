import pygame
from pygame import *
from components.colors import color
from components.chatbox import ChatBox
from components.start import Start

pygame.init()
screen_size = (540, 420)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("ChatBox")

menssage_suf = pygame.Surface((400, 400))

keep_going = True
links = {"start": Start(), "chatbox":ChatBox()}
current_link = "start"
user = ""

while keep_going:
    screen.fill(color.black.value)
    all_event = pygame.event.get()
    for event in all_event:
        if event.type == QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_KP_ENTER]:
                exit()
    current_link, user = links[current_link].run(all_event, screen, screen_size, user)
    pygame.display.update()
