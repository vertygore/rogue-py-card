import pygame as pg
import pygame_widgets as pw
from pygame._sdl2 import Window
from pygame_widgets.button import Button

class UIManager():
    def __init__(self):
        self.clock = pg.time.Clock()  # set up clock
        self.fps = 60
        self.hp_value = 100
        self.win = pg.display.set_mode((640, 480), pg.RESIZABLE)

        self.create_window()

    def create_window(self):
        pg.init()
        Window.from_display_module().maximize()  # maximize window
        margin = 20
        width, height = self.win.get_size() # width und height 

        self.create_buttons()

        # HP BAR SETUP
        hpWidth = 150
        hpHeight = 150
        hpX = self.win.get_width() - hpWidth - margin
        hpY = self.win.get_height() - hpHeight - margin
        hp_border_rect = pg.Rect(hpX, hpY, hpWidth, hpHeight)

        # runtime loop
        running = True
        while running:
            self.clock.tick(self.fps)
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    running = False

            # VISUALS
            self.win.fill((120, 50, 75))  # Hintergrund

            # HP FILL HEIGHT
            fill_height = int((self.hp_value / 100) * hpHeight)
            fill_y = hpY + (hpHeight - fill_height)
            hp_fill_rect = pg.Rect(hpX, fill_y, hpWidth, fill_height)

            # DRAW HP
            pg.draw.rect(self.win, (255, 255, 255), hp_border_rect, width=3)  # Border
            pg.draw.rect(self.win, (0, 200, 0), hp_fill_rect)  # Fill

            pw.update(events)
            pg.display.flip()

    def create_buttons(self):
        margin = 20

        # SETTINGS BUTTON
        settingsWidth = 100
        settingsHeight = 100
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
        testHpWidth = 100
        testHpHeight = 100
        testHpX = self.win.get_width() - testHpWidth - margin
        testHpY = margin*2 + settingsHeight
        self.testHp = Button(
            self.win, testHpX, testHpY, testHpWidth, testHpHeight, text='LOSE HP',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.lose_hp()
        )

        # FILL HP BUTTON
        fillHpWidth = 100
        fillHpHeight = 100
        fillHpX = self.win.get_width() - fillHpWidth - margin
        fillHpY = margin*3 + settingsHeight + testHpHeight
        self.fillHp = Button(
            self.win, fillHpX, fillHpY, fillHpWidth, fillHpHeight, text='FILL HP',
            fontSize=20, margin=margin,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: self.fill_hp()
        )

    def lose_hp(self):
        print(f"HP: {self.hp_value} - 5 = {self.hp_value-5}")
        self.hp_value -= 5
        if self.hp_value < 0:
            print(f"HP: ! REACHED ZERO")
            self.hp_value = 0

    def fill_hp(self):
        print(f"HP: RESET TO 100 (FULL)")
        self.hp_value = 100
