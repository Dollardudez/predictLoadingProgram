import pygame
import sys
from button import Button

class EventHandler:

    def __init__(self):
        """
        Constructor for EventHandler.
        """
        self.registeredClickLocation = []
        self.registeredClickEvents = []


    def eventQueue(self):
        """
        Event Queue analysis
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handleQuit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.handleMouseRelease()


    def handleMouseRelease(self):
        """
        Checks for mouse release in registered location,
        calls registered fun. pointer if true
        """
        pos = pygame.mouse.get_pos()
        for i in range(len(self.registeredClickEvents)):
            if(pos[0]>self.registeredClickLocation[i][0] and
                    self.registeredClickLocation[i][1]+100 > pos[1] >
                    self.registeredClickLocation[i][1]):
                self.registeredClickEvents[i]();

    def registerButton(self, button , event):
        """
        registers button coords and event fun. pointer
        :param button: button object being registered
        :param event: event handler being registered
        """
        self.registeredClickLocation.append([button.x , button.y])
        self.registeredClickEvents.append(event)

    def handleQuit(self):
        """
        quits program
        :return:
        """
        pygame.quit()
        sys.exit(1)