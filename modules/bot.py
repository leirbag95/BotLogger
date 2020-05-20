from modules.converter import ButtonConverter, KeyConverter
from modules.services import TMP_FILE
from pynput.mouse import Button, Controller
import pyautogui
import pandas as pd
from tqdm import tqdm
from datetime import datetime as dt


class EventLOG:
    MOUSE_MOVEMENT=0
    BUTTON_PRESSED=1
    BUTTON_RELEASED=2
    MOUSE_SCROLL=3
    KEY_PRESSED=4

class BotLOG:
    
    PATH_DIR_LOGS=".logs/"
    CHUNK_SIZE=10
    
    def __init__(self,filename):
        pyautogui.FAILSAFE=False
        self.mouse = Controller()
        # read log by chunksize method
        self.logs = pd.read_json(TMP_FILE+filename, lines=True, chunksize=self.CHUNK_SIZE)
        pass

    def move_mouse(self, x, y):
        """move mouse to (x,y) position"""
        pyautogui.moveTo(x, y)
    
    def click_button(self, button):
        """simple click from mouse"""
        self.mouse.click(button)
    
    def double_click_button(self, button):
        """double click from mouse"""
        self.mouse.click(button, 2)
    
    def write_key(self, key):
        """press key"""
        pyautogui.write(key)

    def is_mouse_moved(self, current, prev):
        """detect if mouse was moved by user"""
        return prev != current and prev != (-1,-1)

    def read_log(self, datetime=None):
        """
        read_log() loop log file and exec all of its action
        return True if the file was execute with success
        else return (False, datetime)
        """
        prev_button = "" # use for 2-click
        prev_mouse_pos = (-1,-1) # use for detect mouse movement
        press_datetime = 0 # time press button
        for chunck in self.logs:
            for index in range(chunck.shape[0]):
                def resume_at(index, datetime):
                    if datetime != None:
                        return chunck[chunck["datetime"] == datetime].index[0]
                    return index
                index = resume_at(index,datetime)
                log = chunck.iloc[index]
                event_t = log["event_t"]
                if event_t == EventLOG.MOUSE_MOVEMENT:
                    x, y = float(log['x']), float(log['y'])
                    current_mouse_pos = (pyautogui.position()[0],pyautogui.position()[1])
                    if self.is_mouse_moved(current_mouse_pos, prev_mouse_pos):
                        return (False, log["datetime"])
                    self.move_mouse(x, y)
                elif event_t == EventLOG.BUTTON_PRESSED:
                    press_datetime = log["datetime"]
                    button = ButtonConverter(log["button_t"]).to_button_controller()
                    # double click button management
                    if prev_button == event_t:
                        self.double_click_button(button)
                        index += 1
                    else:
                        self.click_button(button)
                elif event_t == EventLOG.BUTTON_RELEASED:
                    button = ButtonConverter(log["button_t"]).to_button_string()
                    x, y = float(log['x']), float(log['y'])
                    release_datetime = log["datetime"]
                    drag_duration = abs(release_datetime - press_datetime)
                    pyautogui.dragTo(x, y, drag_duration.total_seconds(), button=button)
                elif event_t == EventLOG.MOUSE_SCROLL:
                    y_scroll = int(log["y_scroll"])
                    pyautogui.scroll(y_scroll)
                prev_mouse_pos = (int(log['x']),int(log['y']))
                prev_button = event_t
        return (True, None)


    def run(self):
        """
        run() réunit toutes les fonctions nécessaire au lancement du bot et les éxecutes
        """
        return self.read_log()
        
        pass
