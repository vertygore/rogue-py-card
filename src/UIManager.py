import pygame as pg
import pygame_widgets as pw
import pygame_gui as pygui
from pygame._sdl2 import Window
from pygame_widgets.button import Button

# PYGAME_GUI

class UIManager:
    def __init__(self):
        pg.init()

        info = pg.display.Info() 
        self.size = (info.current_w, info.current_h)
        self.window = pg.display.set_mode(self.size, pg.RESIZABLE)
        # Python Card Game Daniel Angelo
        pg.display.set_caption("PYCAGADAAN")

        self.clock = pg.time.Clock()
        self.manager = pygui.UIManager(self.size)

        # Ressourcenwerte
        self.player_hp_value = 100
        self.enemy_hp_value = 100
        self.player_mana_value = 100
        self.enemy_mana_value = 100

        # Buttons erstellen
        self.create_buttons()
        self.create_cards()

        self.running = True
        self.main_loop()

    def create_buttons(self):
        margin = 10
        btn_width, btn_height = 150, 40
        buttons_x = int(self.size[0] - btn_width - margin)
        buttons_y = margin 

        labels = [
            ("LOSE HP (P)", lambda: self.set_ressource("hp", "player")),
            ("FILL HP (P)", lambda: self.set_ressource("hp", "player", filling=True)),
            ("LOSE HP (E)", lambda: self.set_ressource("hp", "enemy")),
            ("FILL HP (E)", lambda: self.set_ressource("hp", "enemy", filling=True)),
            ("LOSE MANA (P)", lambda: self.set_ressource("mana", "player")),
            ("FILL MANA (P)", lambda: self.set_ressource("mana", "player", filling=True)),
            ("LOSE MANA (E)", lambda: self.set_ressource("mana", "enemy")),
            ("FILL MANA (E)", lambda: self.set_ressource("mana", "enemy", filling=True)),
        ]

        self.buttons = []
        for i, (text, callback) in enumerate(labels):
            if i == 0:
                buttons_x = int(self.size[0] - btn_width * 2 - margin * 2)
            elif i % 2 == 0:
                buttons_x = int(self.size[0] - btn_width * 2 - margin * 2)
                buttons_y += int((btn_height + margin))
            else:
                buttons_x = int(self.size[0] - btn_width - margin)

            btn = pygui.elements.UIButton(
                relative_rect=pg.Rect((buttons_x, buttons_y), (btn_width, btn_height)),
                text=text,
                manager=self.manager,
                object_id=f"#btn_{i}"
            )
            self.buttons.append((btn, callback))

    def create_cards(self):
        margin = 10
        handsize = 5
        w_card, h_card = int(self.size[0] / 10), int(self.size[1] / 4)
        total_hand_width = int(handsize * w_card + (handsize-1) * margin)
        buttons_x = int(self.size[0] / 2 - total_hand_width / 2)
        buttons_y = margin

        self.p_handcards = []
        self.e_handcards = []
        for i in range(handsize * 2):
            # RESET
            if i == handsize:
                buttons_y = self.size[1] - margin - h_card
                buttons_x = self.size[0] / 2 - total_hand_width / 2
            
            if i < handsize: # ENEMY
                btn = pygui.elements.UIButton(
                    relative_rect=pg.Rect((buttons_x, buttons_y), (w_card, h_card)),
                    text=f"E CARD {i}",
                    manager=self.manager,
                    object_id=f"#e_hand_{i}"
                )
                buttons_x += w_card + margin
                self.e_handcards.append(btn)
            else:
                p_card_num = i - handsize
                btn = pygui.elements.UIButton(
                    relative_rect=pg.Rect((buttons_x, buttons_y), (w_card, h_card)),
                    text=f"P CARD {p_card_num}",
                    manager=self.manager,
                    object_id=f"#p_hand_{p_card_num}"
                )
                buttons_x += w_card + margin
                self.p_handcards.append(btn)
        
        self.player_combatfield = pygui.elements.UIButton(
            relative_rect=pg.Rect(((int(self.size[0] / 2) - w_card - margin), int(self.size[1] / 2) - h_card / 2), (w_card, h_card)),
                                text=f"P COMBAT",
                                manager=self.manager,
                                object_id=f"#p_combatfield"
        )
        self.enemy_combatfield = pygui.elements.UIButton(
            relative_rect=pg.Rect(((int(self.size[0] / 2) + margin), int(self.size[1] / 2) - h_card / 2), (w_card, h_card)),
                                text=f"E COMBAT",
                                manager=self.manager,
                                object_id=f"#e_combatfield"
        )


    def draw_bars(self):
        bar_width = 150
        bar_height = 200
        margin = 20

        # Player HP
        x = self.size[0] - bar_width - margin
        y = self.size[1] - bar_height - margin
        self.draw_bar(x, y, bar_width, bar_height, self.player_hp_value, (0, 200, 0), "HP (P)")

        # Enemy HP
        x = margin
        y = margin
        self.draw_bar(x, y, bar_width, bar_height, self.enemy_hp_value, (0, 200, 0), "HP (E)")

        # Player Mana
        x = self.size[0] - bar_width - margin
        y = self.size[1] - (bar_height * 2) - (margin * 2)
        self.draw_bar(x, y, bar_width, bar_height, self.player_mana_value, (0, 0, 200), "MANA (P)")

        # Enemy Mana
        x = margin
        y = margin + bar_height + margin
        self.draw_bar(x, y, bar_width, bar_height, self.enemy_mana_value, (0, 0, 200), "MANA (E)")

    def draw_bar(self, x, y, w, h, value, color, label):
        pg.draw.rect(self.window, (255, 255, 255), (x, y, w, h), 2)
        fill_height = int((value / 100) * h)
        fill_y = y + (h - fill_height)
        pg.draw.rect(self.window, color, (x, fill_y, w, fill_height))
        font = pg.font.SysFont(None, 20)
        text_surf = font.render(label, True, (255, 255, 255))
        self.window.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y - 20))

    def set_ressource(self, ressource, owner, loseVal=5, fillVal=100, filling=False):
        if owner == "player":
            if ressource == "hp":
                value = self.player_hp_value
                if not filling:
                    print(f"HP (P): {value} - {loseVal} = {value - 5}")
                    value -= loseVal
                    if value < 0:
                        print(f"HP (P): ! REACHED ZERO")
                        value = 0
                    self.player_hp_value = value
                else:
                    value += fillVal
                    if value > 100:
                        value = 100
                    print("HP (P): RESET TO 100 (FULL)")
                    self.player_hp_value = value
            elif ressource == "mana":
                value = self.player_mana_value
                if not filling:
                    print(f"MANA (P): {value} - {loseVal} = {value - 5}")
                    value -= loseVal
                    if value < 0:
                        print("MANA (P): ! REACHED ZERO")
                        value = 0
                    self.player_mana_value = value
                else:
                    value += fillVal
                    if value > 100:
                        value = 100
                    print("MANA (P): RESET TO 100 (FULL)")
                    self.player_mana_value = value
        elif owner == "enemy":
            if ressource == "hp":
                value = self.enemy_hp_value
                if not filling:
                    print(f"HP (E): {value} - {loseVal} = {value - 5}")
                    value -= loseVal
                    if value < 0:
                        print("HP (E): ! REACHED ZERO")
                        value = 0
                    self.enemy_hp_value = value
                else:
                    value += fillVal
                    if value > 100:
                        value = 100
                    print("HP (E): RESET TO 100 (FULL)")
                    self.enemy_hp_value = value
            elif ressource == "mana":
                value = self.enemy_mana_value
                if not filling:
                    print(f"MANA (E): {value} - {loseVal} = {value - 5}")
                    value -= loseVal
                    if value < 0:
                        print("MANA (E): ! REACHED ZERO")
                        value = 0
                    self.enemy_mana_value = value
                else:
                    value += fillVal
                    if value > 100:
                        value = 100
                    print("MANA (E): RESET TO 100 (FULL)")
                    self.enemy_mana_value = value
        else:
            print("INVALID OWNER FOR LOSE_HP")

    def main_loop(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0 # FPS LIMIT
            for event in pg.event.get():
                if event.type == pg.QUIT: # QUIT APP
                    self.running = False
                elif event.type == pg.VIDEORESIZE: # WINDOW RESIZING
                    self.size = event.size
                    self.window = pg.display.set_mode(self.size, pg.RESIZABLE)
                    self.manager.set_window_resolution(self.size)
                    self.manager.clear_and_reset()
                    self.create_buttons()
                    self.create_cards()
                elif event.type == pygui.UI_BUTTON_PRESSED: # BUTTON EVENT HANDLING
                    for btn, callback in self.buttons:
                        if event.ui_element == btn:
                            callback()
                    if event.ui_object_id.startswith("#e_hand_"):
                        print(f"CLICKED E CARD {event.ui_object_id}")
                    elif event.ui_object_id.startswith("#p_hand_"):
                        print(f"CLICKED P CARD {event.ui_object_id}")
                    elif event.ui_object_id.startswith("#e_combatfield"):
                        print(f"CLICKED E COMBATFIELD {event.ui_object_id}")
                    elif event.ui_object_id.startswith("#p_combatfield"):
                        print(f"CLICKED P COMBATFIELD {event.ui_object_id}")


                self.manager.process_events(event)
                self.manager.update(time_delta)
                self.window.fill((30, 30, 30))
                self.draw_bars()
                self.manager.draw_ui(self.window)

            pg.display.update()


if __name__ == "__main__":
    UIManager()

