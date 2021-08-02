import pygame
import os

#load img
MENU_IMG=pygame.image.load(os.path.join("images", "upgrade_menu.png"))
SELL_IMG=pygame.image.load(os.path.join("images", "sell.png"))
UPGRADE_IMG=pygame.image.load(os.path.join("images", "upgrade.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.width =200
        self.height =200
        self.center=(x,y)
        self.img = pygame.transform.scale(MENU_IMG, (self.width, self.height))
        self.rect=self.img.get_rect()
        self.rect.center=self.center
        self.__buttons = self.init_buttons()  # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.img,(self.center[0]-self.width/2,self.center[1]-self.height/2))
        # draw button
        # (Q2) Draw buttons here
        
        #blit the buttons on the win
        for button in self.__buttons:
            win.blit(button.img,button.rect.topleft)

        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        pass

    def init_buttons(self):
        """
        create the default buttons and return the new __buttons
        """
        btn_list=[]

        #instantiate the sell button
        btn_img=pygame.transform.scale(SELL_IMG, (50, 50))
        btn_list.append(Button(btn_img, "sell", self.center[0], self.center[1]-70))

        #instantiate the upgrade button
        btn_img=pygame.transform.scale(UPGRADE_IMG, (80, 50))
        btn_list.append(Button(btn_img, "upgrade", self.center[0],self.center[1]+75))
        return btn_list
        
class Button:
    def __init__(self, image, name, x, y):
        self.name = name

        self.center=(x, y)
        self.img=image
        self.rect=self.img.get_rect()
        self.rect.center=self.center

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return self.rect.collidepoint(x,y)
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass






