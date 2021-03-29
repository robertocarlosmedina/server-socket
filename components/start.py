import pygame
from pygame.locals import *
from components.colors import color, rgbColor
from components.textInput import Textinput
from components.buttons import verticalButtonsDisplay


class Start:
    pygame.init()
    y1, x1 = None, None
    text = Textinput()


    def __init__(self):
        self.size = 60
        self.box_info = []
        self.x, self.y = 260, 150
        self.changeColor = True
        self.font = pygame.font.SysFont("arial", 30)
        self.timer = 0
        self.user = " "
        self.created = False
        self.buttons = ["Log"]

    def run(self, all_event, screen, screen_size, user):
        del user
        mouse_pos = pygame.mouse.get_pos()
        for event in all_event:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_RETURN]:
                    self.created = True
        size = pygame.font.Font.size(self.font, 'AlgorDataStruct')
        line = self.font.render('AlgorDataStruct', True, color.white.value)
        screen.blit(line, (int(screen_size[0]/2-size[0]/2), int(screen_size[1]/2-size[1]/2)-60))
        self.user = self.text.settingInputText(all_event, screen)
        
        verticalButtonsDisplay(screen, self.buttons, 205, (int(screen_size[0]/2), int(screen_size[1]/2)), (150, 40),mouse_pos, " ", self.font)
        if self.created:
            return "chatbox", self.user
        else:
            return "start", self.user
            