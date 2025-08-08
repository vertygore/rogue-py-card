import pygame as pg
import pygame_gui as pygui

class EventHandler:
    def __init__(self, ui_manager, ingame, manager, window, gameStateManager, gameloop):
        self.ui_manager = ui_manager
        self.ingame = ingame
        self.manager = manager
        self.window = window
        self.gameStateManager = gameStateManager
        self.gameloop = gameloop

    def handle_ingame_event(self, event):
        if event.type == pg.QUIT:
            self.ui_manager.running = False
        elif event.type == pg.VIDEORESIZE:
            size = event.size
            self.window = pg.display.set_mode(size, pg.RESIZABLE)
            self.manager.set_window_resolution(size)
            self.manager.clear_and_reset()
            self.ingame.size = size
            self.ingame.initialized = False
        elif event.type == pygui.UI_BUTTON_PRESSED:
            state = self.ui_manager.states[self.gameStateManager.get_state()]
            if hasattr(state, 'buttons'):
                for btn, callback in state.buttons:
                    if event.ui_element == btn:
                        callback()
            if event.ui_object_id.startswith("#e_hand_"):
                print(f"CLICKED E CARD {event.ui_object_id}")
            elif event.ui_object_id.startswith("#p_hand_"):
                print(f"CLICKED P CARD {event.ui_object_id}")
                self.drawncards = self.gameloop.execute_turn(int(event.ui_object_id[-1]))
                print(self.drawncards)
            elif event.ui_object_id.startswith("#e_combatfield"):
                print(f"CLICKED E COMBATFIELD {event.ui_object_id}")
            elif event.ui_object_id.startswith("#p_combatfield"):
                print(f"CLICKED P COMBATFIELD {event.ui_object_id}")
            else:
                print(f"CLICKED UNKOWN FIELD {event.ui_object_id}")
