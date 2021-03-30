import pygame
import os
from pygame.locals import *
from serversSockets.tcp import client
from components.colors import color
from components.textInput import Textinput


class ChatBox:
    pygame.init()
    # base_font = pygame.font.Font("/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
    base_font = pygame.font.SysFont("arial", 18)
    user = client.User()
    text = Textinput()
    send = False
    event = None
    all_menssage = None
    menssage_suf = pygame.Surface((400, 400))
    userName = ""
    start = True

    def run(self, all_event, screen, screen_size, user):
        t = ''
        self.userName = user
        self.menssage_suf.fill(color.grey1.value)
        for event in all_event:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_RETURN]:
                    self.send = True

        t = self.text.settingInputText(all_event, self.menssage_suf, (30, 355, 340))

        if self.send or self.start:
            self.all_menssage = self.user.serverConectAndSend(t+'-'+self.userName)
            self.send = False
            self.start = False
        self.menssageDisplay()
        screen.blit(self.menssage_suf, (int(screen_size[0]/2-200), int(screen_size[1]/2-200)))
        return "chatbox", self.userName

    def menssageDisplay(self):
        y = 320
        if self.all_menssage!=None:
            msgs = self.all_menssage.split("/")
            msgs = msgs[::-1]
            for msg in msgs:
                text_surface = self.base_font.render(msg, True, (255, 255, 255))
                size = pygame.font.Font.size(self.base_font, str(msg))
            
                # pygame.draw.rect(self.menssage_suf, color.green.value, button_box)

                sender = msg.split("-")
                if len(sender)==2:
                    msg = sender[0]
                    sender = sender[1]
                    text_surface = self.base_font.render(msg, True, (255, 255, 255))
                    size = pygame.font.Font.size(self.base_font, str(msg))
                    button_box = pygame.Rect(size[0]-20, y-20, size[0]+20, size[1]+20)
                    
                if sender==self.userName.lower():
                    button_box = pygame.Rect(int(400/2-size[0]/2)+100-10, y, size[0]+20, size[1])
                    pygame.draw.rect(self.menssage_suf, color.green.value, button_box)
                    self.menssage_suf.blit(text_surface, (int(400/2-size[0]/2)+100, y))
                else:
                    button_box = pygame.Rect(int(400/2-size[0]/2)-100-10, y-20, size[0]+20, size[1])
                    pygame.draw.rect(self.menssage_suf, color.green.value, button_box)
                    self.menssage_suf.blit(text_surface, (int(400/2-size[0]/2)-100, y))

                y -= 30