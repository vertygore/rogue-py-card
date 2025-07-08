import pygame as pg
import pygame_widgets as pw
from pygame._sdl2 import Window
from pygame_widgets.button import Button

class UIManager():
    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()  # set up clock
        self.fps = 60
        self.margin = 20
        self.player_hp_value = 100
        self.enemy_hp_value = 100
        info = pg.display.Info()  # Infos zum Bildschirm
        self.width, self.height = info.current_w, info.current_h
        self.win = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.delta_time = 0.1
        self.default_btn_dim = 100
        self.playerhand = []
        self.enemyhand = []

        self.create_window()

    def create_window(self):
        win = self.win
        margin = 20

        self.create_buttons()

        # HP BAR SETUP (als Attribute speichern, damit du sie anpassen kannst)
        self.hpWidth = 150
        self.player_hpHeight = 150
        self.enemy_hpHeight = 150
        self.margin = margin

        running = True
        while running:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.VIDEORESIZE:
                    # Fenstergröße anpassen
                    self.width, self.height = event.w, event.h
                    self.win = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
                    self.create_buttons()
                    

            # VISUALS
            self.win.fill((120, 50, 75))

            # HP BARS
            # Spieler HP
            player_hpX = self.width - self.hpWidth - self.margin
            player_hpY = self.height - self.player_hpHeight - self.margin
            player_fill_height = int((self.player_hp_value / 100) * self.player_hpHeight)
            player_fill_y = player_hpY + (self.player_hpHeight - player_fill_height)
            player_hp_border_rect = pg.Rect(player_hpX, player_hpY, self.hpWidth, self.player_hpHeight)
            player_hp_fill_rect = pg.Rect(player_hpX, player_fill_y, self.hpWidth, player_fill_height)

            # Gegner HP
            enemy_hpX = self.margin
            enemy_hpY = self.margin
            enemy_fill_height = int((self.enemy_hp_value / 100) * self.enemy_hpHeight)
            enemy_fill_y = enemy_hpY + (self.enemy_hpHeight - enemy_fill_height)
            enemy_hp_border_rect = pg.Rect(enemy_hpX, enemy_hpY, self.hpWidth, self.enemy_hpHeight)
            enemy_hp_fill_rect = pg.Rect(enemy_hpX, enemy_fill_y, self.hpWidth, enemy_fill_height)

            # Zeichnen
            pg.draw.rect(self.win, (255, 255, 255), player_hp_border_rect, width=3)
            pg.draw.rect(self.win, (0, 200, 0), player_hp_fill_rect)
            pg.draw.rect(self.win, (255, 255, 255), enemy_hp_border_rect, width=3)
            pg.draw.rect(self.win, (0, 200, 0), enemy_hp_fill_rect)

            pw.update(events)
            pg.display.flip()
            self.clock.tick(self.fps)

        pg.quit()

    def create_buttons(self):
        margin = 20

        # SETTINGS BUTTON
        settingsWidth = self.default_btn_dim
        settingsHeight = self.default_btn_dim
        settingsX = self.win.get_width() - settingsWidth - margin
        settingsY = margin
        self.settingsBtn = Button(
            self.win, settingsX, settingsY, settingsWidth, settingsHeight, text='SETTINGS',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: print("Clicked SETTINGS")
        )

        # LOSE HP BUTTON
        player_testHpWidth = self.default_btn_dim
        player_testHpHeight = self.default_btn_dim
        player_testHpX = self.win.get_width() - player_testHpWidth - margin
        player_testHpY = margin*2 + settingsHeight
        self.player_testHp = Button(
            self.win, player_testHpX, player_testHpY, player_testHpWidth, player_testHpHeight, text='LOSE HP (P)',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.lose_hp()
        )

        # FILL HP BUTTON
        player_fillHpWidth = self.default_btn_dim
        player_fillHpHeight = self.default_btn_dim
        player_fillHpX = self.win.get_width() - player_fillHpWidth - margin
        player_fillHpY = margin*3 + settingsHeight + player_testHpHeight
        self.player_fillHp = Button(
            self.win, player_fillHpX, player_fillHpY, player_fillHpWidth, player_fillHpHeight, text='FILL HP (P)',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.fill_hp()
        )

        # LOSE ENEMY HP BUTTON
        enemy_testHpWidth = self.default_btn_dim
        enemy_testHpHeight = self.default_btn_dim
        enemy_testHpX = self.win.get_width() - enemy_testHpWidth*2 - margin*2
        enemy_testHpY = margin*2 + settingsHeight
        self.enemy_testHp = Button(
            self.win, enemy_testHpX, enemy_testHpY, enemy_testHpWidth, enemy_testHpHeight, text='LOSE HP (E)',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.lose_hp(owner="enemy")
        )

        # FILL ENEMY HP BUTTON
        enemy_fillHpWidth = self.default_btn_dim
        enemy_fillHpHeight = self.default_btn_dim
        enemy_fillHpX = self.win.get_width() - enemy_fillHpWidth*2 - margin*2
        enemy_fillHpY = margin*3 + settingsHeight + enemy_testHpHeight
        self.enemy_fillHp = Button(
            self.win, enemy_fillHpX, enemy_fillHpY, enemy_fillHpWidth, enemy_fillHpHeight, text='FILL HP (E)',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.fill_hp(owner="enemy")
        )

        # HANDS
        # UTIL
        handsize = 5
        card_width = self.width / 10
        card_height = self.width / 5
        card_xanchor = self.width / 2 - (card_width / 2)*handsize
        handoffset_x = card_width + self.margin

        # PLAYER
        card_yanchor = self.height - card_height - self.margin
        for i in range(handsize):
            self.playerhand.append(Button(self.win, card_xanchor + (handoffset_x * i), card_yanchor, card_width, card_height, text=f"EMPTY {i}", 
                                     fontSize=20, margin=margin, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0), 
                                     radius=20, onClick=lambda i=i: print(f"CLICKED PLAYER CARD {i}")))
        
        # ENEMY
        card_yanchor = self.margin
        for i in range(handsize):
            self.enemyhand.append(Button(self.win, card_xanchor + (handoffset_x * i), card_yanchor, card_width, card_height, text=f"EMPTY {i}", 
                                     fontSize=20, margin=margin, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0), 
                                     radius=20, onClick=lambda i=i: print(f"CLICKED ENEMY CARD {i}")))

        # ENEMY

    def lose_hp(self, owner="player"):
        if owner == "player":
            hp_value = self.player_hp_value
            print(f"HP: {hp_value} - 5 = {hp_value-5}")
            hp_value -= 5
            if hp_value < 0:
                print(f"HP: ! REACHED ZERO")
                hp_value = 0
            self.player_hp_value = hp_value
        elif owner == "enemy":
            hp_value = self.enemy_hp_value
            print(f"HP: {hp_value} - 5 = {hp_value-5}")
            hp_value -= 5
            if hp_value < 0:
                print(f"HP: ! REACHED ZERO")
                hp_value = 0
            self.enemy_hp_value = hp_value
        else:
            print(f"INVALID OWNER FOR LOSE_HP")
            return None
        
        
        


    def fill_hp(self, owner="player"):
        if owner == "player":
            self.player_hp_value = 100
        elif owner == "enemy":
            self.enemy_hp_value = 100
        else:
            print(f"INVALID OWNER FOR LOSE_HP")
            return None
        print(f"HP: RESET TO 100 (FULL)")
        
        
