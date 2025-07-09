import pygame as pg
import pygame_widgets as pw
from pygame._sdl2 import Window
from pygame_widgets.button import Button


class UIManager():
    def __init__(self):
        """
        Initialisiert pygame und setzt alle wichtigen Grundvariablen wie benötigt
        """
        pg.init()

        self.clock = pg.time.Clock()  # Clock damit der Loop nur 60x pro Sekunde ausgeführt wird
        info = pg.display.Info() 
        self.width, self.height = info.current_w, info.current_h
        self.win = pg.display.set_mode((self.width, self.height), pg.RESIZABLE) # Damit das Fenster Maximized werden kann
        
        # default Variablen
        self.default_btn_dim = 75
        self.default_fontsize = 12
        self.fps = 60
        self.margin = 20
        self.player_hp_value = 100
        self.enemy_hp_value = 100
        self.player_mana_value = 100
        self.enemy_mana_value = 100
        self.player_mana_value = 100
        self.enemy_mana_value = 100
        self.playerhand = []
        self.enemyhand = []

        self.create_window()

    def create_window(self):
        """
        Erstellt das Fenster der Appliaktion und listened nach Events die auftauchen
        """
        win = self.win
        margin = 20

        self.create_buttons()

        # HP BAR SETUP (als Attribute speichern, damit du sie anpassen kannst)
        self.hpWidth = 150
        self.player_hpHeight = 150
        self.enemy_hpHeight = 150
        self.manaWidth = 150
        self.player_manaHeight = 150
        self.enemy_manaHeight = 150
        self.margin = margin

        # GAME LOOP
        running = True
        while running:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT: # Fenster schließen
                    running = False
                elif event.type == pg.VIDEORESIZE: # Fenstergröße ändern
                    self.width, self.height = event.w, event.h
                    self.win = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
                    self.create_buttons()
                    

            # VISUALS
            self.win.fill((120, 50, 75))

            # BARS
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

            # Spieler Mana
            player_manaX = self.width - self.manaWidth - self.margin
            player_manaY = self.height - self.player_manaHeight - self.margin - self.player_manaHeight
            player_mana_fill_height = int((self.player_mana_value / 100) * self.player_manaHeight)
            player_mana_fill_y = player_manaY + (self.player_manaHeight - player_mana_fill_height)
            player_mana_border_rect = pg.Rect(player_manaX, player_manaY, self.manaWidth, self.player_manaHeight)
            player_mana_fill_rect = pg.Rect(player_manaX, player_mana_fill_y, self.manaWidth, player_mana_fill_height)

            # Gegner Mana
            enemy_manaX = self.margin
            enemy_manaY = self.margin + self.enemy_manaHeight
            enemy_mana_fill_height = int((self.enemy_mana_value / 100) * self.enemy_manaHeight)
            enemy_mana_fill_y = enemy_manaY + (self.enemy_manaHeight - enemy_mana_fill_height)
            enemy_mana_border_rect = pg.Rect(enemy_manaX, enemy_manaY, self.manaWidth, self.enemy_manaHeight)
            enemy_mana_fill_rect = pg.Rect(enemy_manaX, enemy_mana_fill_y, self.manaWidth, enemy_mana_fill_height)

            # Render
            pg.draw.rect(self.win, (255, 255, 255), player_hp_border_rect, width=3)
            pg.draw.rect(self.win, (0, 200, 0), player_hp_fill_rect)
            pg.draw.rect(self.win, (255, 255, 255), enemy_hp_border_rect, width=3)
            pg.draw.rect(self.win, (0, 200, 0), enemy_hp_fill_rect)
            pg.draw.rect(self.win, (255, 255, 255), player_mana_border_rect, width=3)
            pg.draw.rect(self.win, (0, 0, 200), player_mana_fill_rect)
            pg.draw.rect(self.win, (255, 255, 255), enemy_mana_border_rect, width=3)
            pg.draw.rect(self.win, (0, 0, 200), enemy_mana_fill_rect)

            # Refresh
            pw.update(events)
            pg.display.flip()
            self.clock.tick(self.fps)

        pg.quit()

    def create_buttons(self):
        """
        Erstellt alle Buttons die auf einem Spielfeld vorhanden sind und positioniert sie
        """
        margin = 20
        self.playerhand.clear()
        self.enemyhand.clear()

        # UI BUTTONS

        # SETTINGS BUTTON
        settingsX = self.win.get_width() - self.default_btn_dim - margin
        settingsY = margin
        self.settingsBtn = Button(
            self.win, settingsX, settingsY, self.default_btn_dim, self.default_btn_dim, text='SETTINGS',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: print("Clicked SETTINGS")
        )

        # LOSE HP BUTTON
        player_testHpX = self.win.get_width() - self.default_btn_dim - margin
        player_testHpY = margin*2 + self.default_btn_dim
        self.player_testHp = Button(
            self.win, player_testHpX, player_testHpY, self.default_btn_dim, self.default_btn_dim, text='LOSE HP (P)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="hp", owner="player")
        )

        # FILL HP BUTTON
        player_fillHpX = self.win.get_width() - self.default_btn_dim - margin
        player_fillHpY = margin*3 + self.default_btn_dim*2
        self.player_fillHp = Button(
            self.win, player_fillHpX, player_fillHpY, self.default_btn_dim, self.default_btn_dim, text='FILL HP (P)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="hp", owner="player", filling=True)
        )

        # LOSE ENEMY HP BUTTON
        enemy_testHpX = self.win.get_width() - self.default_btn_dim*2 - margin*2
        enemy_testHpY = margin*2 + self.default_btn_dim
        self.enemy_testHp = Button(
            self.win, enemy_testHpX, enemy_testHpY, self.default_btn_dim, self.default_btn_dim, text='LOSE HP (E)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="hp", owner="enemy")
        )

        # FILL ENEMY HP BUTTON
        enemy_fillHpX = self.win.get_width() - self.default_btn_dim*2 - margin*2
        enemy_fillHpY = margin*3 + self.default_btn_dim*2
        self.enemy_fillHp = Button(
            self.win, enemy_fillHpX, enemy_fillHpY, self.default_btn_dim, self.default_btn_dim, text='FILL HP (E)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="hp", owner="enemy", filling=True)
        )

        # LOSE MANA BUTTON 
        player_testManaX = self.win.get_width() - self.default_btn_dim - margin
        player_testManaY = margin*4 + self.default_btn_dim*3
        self.player_testMana = Button(
            self.win, player_testManaX, player_testManaY, self.default_btn_dim, self.default_btn_dim, text='LOSE MANA (P)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="mana", owner="player")
        )

        # FILL MANA BUTTON
        player_fillManaX = self.win.get_width() - self.default_btn_dim - margin
        player_fillManaY = margin*5 + self.default_btn_dim*4
        self.player_fillMana = Button(
            self.win, player_fillManaX, player_fillManaY, self.default_btn_dim, self.default_btn_dim, text='FILL MANA (P)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="mana", owner="player", filling=True)
        )

        # LOSE ENEMY MANA BUTTON
        enemy_testManaX = self.win.get_width() - self.default_btn_dim*2 - margin*2
        enemy_testManaY = margin*4 + self.default_btn_dim*3
        self.enemy_testMana = Button(
            self.win, enemy_testManaX, enemy_testManaY, self.default_btn_dim, self.default_btn_dim, text='LOSE MANA (E)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="mana", owner="enemy")
        )

        # FILL ENEMY MANA BUTTON
        enemy_fillManaX = self.win.get_width() - self.default_btn_dim*2 - margin*2
        enemy_fillManaY = margin*5 + self.default_btn_dim*4
        self.enemy_fillMana = Button(
            self.win, enemy_fillManaX, enemy_fillManaY, self.default_btn_dim, self.default_btn_dim, text='FILL MANA (E)',
            fontSize=self.default_fontsize, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.set_ressource(ressource="mana", owner="enemy", filling=True)
        )

        # HANDS
        # UTIL
        handsize = 5
        card_width = self.width / 10
        card_height = self.width / 8
        total_hand_width = handsize * card_width + (handsize - 1) * margin
        card_xanchor = self.width / 2 - total_hand_width / 2
        handoffset_x = card_width + margin

        # PLAYER
        card_yanchor = self.height - card_height - margin
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

        self.player_combatfield = Button(self.win, (self.width / 2 - card_width / 2) - card_width / 2 - margin, self.height / 2 - card_height / 2, card_width, card_height, text=f"P COMBAT",
                                    fontSize=20, margin=margin, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0),
                                    radius=20, onClick=lambda: print(f"CLICKED PLAYER COMBAT FIELD"))
        
        self.enemy_combatfield = Button(self.win, (self.width / 2 - card_width / 2) + card_width / 2 + margin, self.height / 2 - card_height / 2, card_width, card_height, text=f"E COMBAT",
                                    fontSize=20, margin=margin, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0),
                                    radius=20, onClick=lambda: print(f"CLICKED ENEMY COMBAT FIELD"))
        

    def set_ressource(self, ressource, owner, loseVal=5, fillVal=100, filling=False):
        if owner == "player": # Player?
            if ressource == "hp": # HP?
                value = self.player_hp_value
                if filling == False: # Addieren?
                    print(f"HP (P): {value} - {loseVal} = {value-5}")
                    value -= loseVal
                    if value < 0: # Leer?
                        print(f"HP (P): ! REACHED ZERO")
                        value = 0
                    self.player_hp_value = value
                else: # Subtrahieren?
                    value += fillVal
                    if value > 100: # Voll?
                        value = 100
                    print(f"HP (P): RESET TO 100 (FULL)")
                    self.player_hp_value = value
            elif ressource == "mana": # Mana?
                value = self.player_mana_value
                if filling == False: # Addieren?
                    print(f"MANA (P): {value} - {loseVal} = {value-5}")
                    value -= loseVal
                    if value < 0: # Leer?
                        print(f"MANA (P): ! REACHED ZERO")
                        value = 0
                    self.player_mana_value = value
                else: # Subtrahieren?
                    value += fillVal
                    if value > 100: # Voll?
                        value = 100
                    print(f"MANA (P): RESET TO 100 (FULL)")
                    self.player_mana_value = value
        elif owner == "enemy": # Enemy ?
            if ressource == "hp": # HP ?
                value = self.enemy_hp_value
                if filling == False: # Addieren?
                    print(f"HP (E): {value} - {loseVal} = {value-5}")
                    value -= loseVal
                    if value < 0: # Leer?
                        print(f"HP (E): ! REACHED ZERO")
                        value = 0
                    self.enemy_hp_value = value
                else: # Subtrahieren?
                    value += fillVal
                    if value > 100: # Voll?
                        value = 100
                    print(f"HP (E): RESET TO 100 (FULL)")
                    self.enemy_hp_value = value
            elif ressource == "mana": # Mana?
                value = self.enemy_mana_value
                if filling == False: # Addieren?
                    print(f"MANA (E): {value} - {loseVal} = {value-5}")
                    value -= loseVal
                    if value < 0: # Leer?
                        print(f"MANA (E): ! REACHED ZERO")
                        value = 0
                    self.enemy_mana_value = value
                else: # Subtrahieren?
                    value += fillVal
                    if value > 100: # Voll?
                        value = 100
                    print(f"MANA (E): RESET TO 100 (FULL)")
                    self.enemy_mana_value = value
        else: # INVALID OWNER?
            print(f"INVALID OWNER FOR LOSE_HP")
            return None
