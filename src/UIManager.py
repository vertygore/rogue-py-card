import pygame as pg
import pygame_gui as pygui
from src.Gameloop import GameLoop
from src.Enemy import Enemy
from src.Player import Player
from pygame._sdl2 import Window

class UIManager:
    """
    Handles everything UI related
    """
    def __init__(self):
        pg.init()

        # Init Game Logic
        self.gameloop = GameLoop()

        # Init Display
        info = pg.display.Info() 
        self.size = (info.current_w, info.current_h)
        self.window = pg.display.set_mode(self.size, pg.RESIZABLE)
        pg.display.set_caption("PYCAGADAAN")

        # Init UI Util
        self.manager = pygui.UIManager(self.size)
        self.gameStateManager = GameStateManager('mainmenu')
        self.ingame = Ingame(self.window, self.gameStateManager, self.size, self.manager, self.gameloop)
        self.mainmenu = MainMenu(self.window, self.gameStateManager)
        self.states = {'mainmenu': self.mainmenu, 'ingame': self.ingame}
        self.clock = pg.time.Clock()

        # Start App (+ Loop)
        self.running = True
        self.main_loop()

    def main_loop(self):
        """
        Starts the main game loop, refreshing 60 times per second
        """
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0 # Time Manipulation, Frame Limit
            # EVENT HANDLING
            for event in pg.event.get():
                if event.type == pg.QUIT: # Quit App
                    self.running = False
                elif event.type == pg.VIDEORESIZE: # Resize Win
                    self.size = event.size
                    self.window = pg.display.set_mode(self.size, pg.RESIZABLE)
                    self.manager.set_window_resolution(self.size)
                    self.manager.clear_and_reset()
                    self.ingame.size = self.size
                    self.ingame.initialized = False
                elif event.type == pygui.UI_BUTTON_PRESSED: # UI Buttons
                    state = self.states[self.gameStateManager.get_state()]
                    if hasattr(state, 'buttons'): # General UI
                        for btn, callback in state.buttons:
                            if event.ui_element == btn:
                                callback()
                    if event.ui_object_id.startswith("#e_hand_"): # Enemy Hand
                        print(f"CLICKED E CARD {event.ui_object_id}")
                    elif event.ui_object_id.startswith("#p_hand_"): # Player Hand
                        print(f"CLICKED P CARD {event.ui_object_id}")
                        self.gameloop.execute_turn(int(event.ui_object_id[-1]))
                    elif event.ui_object_id.startswith("#e_combatfield"): # Enemy Combatfield
                        print(f"CLICKED E COMBATFIELD {event.ui_object_id}")
                    elif event.ui_object_id.startswith("#p_combatfield"): # Player Combatfield
                        print(f"CLICKED P COMBATFIELD {event.ui_object_id}")
                        print(self.drawncards)

                self.states[self.gameStateManager.get_state()].run() # State Update

                # Process Everything
                self.manager.process_events(event)
                self.manager.update(time_delta)
                self.manager.draw_ui(self.window)

            # Update Graphics
            pg.display.update()


class Ingame():
    """
    Handles the UI for Ingame
    """
    def __init__(self, display, gameStateManager, size, manager, gameloop):
        # Util vars
        self.display = display
        self.gameStateManager = gameStateManager
        self.size = size
        self.manager = manager
        self.gameloop = gameloop
        self.player_hp_value = 100
        self.enemy_hp_value = 100
        self.player_mana_value = 100
        self.enemy_mana_value = 100
        self.buttons = []
        self.p_handcards = []
        self.e_handcards = []
        self.initialized = False


    def run(self):
        self.display.fill((30, 30, 30)) # BG Color

        # Init UI
        if not self.initialized:
            self.create_buttons()
            self.create_cards()
            self.initialized = True
        self.draw_bars()

    def create_buttons(self):
        # Util var
        margin = 10
        btn_width, btn_height = 150, 40
        buttons_x = int(self.size[0] - btn_width - margin)
        buttons_y = margin 

        labels = [
            ("LOSE HP (P)", lambda: self.set_ressource("hp", "player")),
            ("FILL HP (P)", lambda: self.set_ressource("hp", "player", modVal=100, filling=True)),
            ("LOSE HP (E)", lambda: self.set_ressource("hp", "enemy")),
            ("FILL HP (E)", lambda: self.set_ressource("hp", "enemy", modVal=100, filling=True)),
            ("LOSE MANA (P)", lambda: self.set_ressource("mana", "player")),
            ("FILL MANA (P)", lambda: self.set_ressource("mana", "player", modVal=100, filling=True)),
            ("LOSE MANA (E)", lambda: self.set_ressource("mana", "enemy")),
            ("FILL MANA (E)", lambda: self.set_ressource("mana", "enemy", modVal=100, filling=True)),
        ]

        # Create UI Buttons
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
        """
        Creates all card buttons (enemy hand, player hand, enemy combatfield, player combatfield)
        and positions them
        """

        self.gameloop.refill_hands()

        # Util var
        margin = 10
        handsize = 5
        w_card, h_card = int(self.size[0] / 10), int(self.size[1] / 4)
        total_hand_width = int(handsize * w_card + (handsize - 1) * margin)
        buttons_x = int(self.size[0] / 2 - total_hand_width / 2)
        buttons_y = margin

        # Create Card Buttons
        for i in range(handsize * 2):
            if i == handsize: # Anchor Reset for Player Cards
                buttons_y = self.size[1] - margin - h_card
                buttons_x = self.size[0] / 2 - total_hand_width / 2

            if i < handsize: # Enemy
                btn = pygui.elements.UIButton(
                    relative_rect=pg.Rect((buttons_x, buttons_y), (w_card, h_card)),
                    text=f"E CARD {i}",
                    manager=self.manager,
                    object_id=f"#e_hand_{i}"
                )
                self.e_handcards.append(btn)
            else: # Player
                p_card_num = i - handsize
                btn = pygui.elements.UIButton(
                    relative_rect=pg.Rect((buttons_x, buttons_y), (w_card, h_card)),
                    text=f"P CARD {p_card_num}",
                    manager=self.manager,
                    object_id=f"#p_hand_{p_card_num}"
                )
                self.p_handcards.append(btn)

            buttons_x += w_card + margin # Offset for Positioning

        # Combatfields
        # Player
        self.player_combatfield = pygui.elements.UIButton(
            relative_rect=pg.Rect(((int(self.size[0] / 2) - w_card - margin), int(self.size[1] / 2) - h_card / 2), (w_card, h_card)),
            text=f"P COMBAT",
            manager=self.manager,
            object_id=f"#p_combatfield"
        )

        # Enemy
        self.enemy_combatfield = pygui.elements.UIButton(
            relative_rect=pg.Rect(((int(self.size[0] / 2) + margin), int(self.size[1] / 2) - h_card / 2), (w_card, h_card)),
            text=f"E COMBAT",
            manager=self.manager,
            object_id=f"#e_combatfield"
        )

    def draw_bars(self):
        """
        Creates Positions all HP and Mana bars on the field
        """
        bar_width = 150
        bar_height = 200
        margin = 20

        x = self.size[0] - bar_width - margin
        y = self.size[1] - bar_height - margin
        self.draw_bar(x, y, bar_width, bar_height, self.player_hp_value, (0, 200, 0), "HP (P)")

        x = margin
        y = margin
        self.draw_bar(x, y, bar_width, bar_height, self.enemy_hp_value, (0, 200, 0), "HP (E)")

        x = self.size[0] - bar_width - margin
        y = self.size[1] - (bar_height * 2) - (margin * 2)
        self.draw_bar(x, y, bar_width, bar_height, self.player_mana_value, (0, 0, 200), "MANA (P)")

        x = margin
        y = margin + bar_height + margin
        self.draw_bar(x, y, bar_width, bar_height, self.enemy_mana_value, (0, 0, 200), "MANA (E)")

    def draw_bar(self, x, y, w, h, value, color, label):
        """
        Constructor for a Mana or HP bar
        """
        pg.draw.rect(self.display, (0, 0, 0), (x, y, w, h)) 
        pg.draw.rect(self.display, (255, 255, 255), (x, y, w, h), 2)

        fill_height = int((value / 100) * h)
        fill_y = y + (h - fill_height)
        pg.draw.rect(self.display, color, (x, fill_y, w, fill_height))

        font = pg.font.SysFont(None, 20)
        text_surf = font.render(label, True, (255, 255, 255))
        self.display.blit(text_surf, (x + (w - text_surf.get_width()) // 2, y - 20))

    def set_ressource(self, ressource, owner, modVal=5, filling=False):
        """
        TESTING METHOD:
        function for test buttons, manipulates ressources (mana or hp) for either the player or the enemy
        
        filling: False = subtract, True = add
        """
        fillingMult = 1
        if not filling:
            fillingMult = -1

        if owner == "player":
            if ressource == "hp":
                self.player_hp_value = min(max(self.player_hp_value + modVal * fillingMult, 0), 100)
            elif ressource == "mana":
                self.player_mana_value = min(max(self.player_mana_value + modVal * fillingMult, 0), 100)
        elif owner == "enemy":
            if ressource == "hp":
                self.enemy_hp_value = min(max(self.enemy_hp_value + modVal * fillingMult, 0), 100)
            elif ressource == "mana":
                self.enemy_mana_value = min(max(self.enemy_mana_value + modVal * fillingMult, 0), 100)


class MainMenu():
    """
    Handles the UI for the Main Menu
    """
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.font = pg.font.SysFont(None, 80)

    def run(self):
        self.display.fill((0, 0, 0))

        title_text = self.font.render("E ZUM SPIEL STARTEN", True, (255, 255, 255))
        text_rect = title_text.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 2))
        self.display.blit(title_text, text_rect)

        keys = pg.key.get_pressed()
        if keys[pg.K_e]:
            self.gameStateManager.set_state('ingame')


class GameStateManager():
    """
    Saves GameStates (Scenes)
    """
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


if __name__ == "__main__":
    UIManager()
