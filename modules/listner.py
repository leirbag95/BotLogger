from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener
import logging
import os


class ListenerLOG:

    def __init__(self, filename):
        if not os.path.exists('.logs/'):
            os.mkdir('.logs/')
        # ['datetime', 'x_mouse', 'y_mouse', 'event_t','click_t', 'dx', 'dy', 'key']
        logging.basicConfig(filename=".logs/"+filename, 
                            level=logging.DEBUG, 
                            format='{"datetime":"%(asctime)s",%(message)s}')

    def on_move(self, x, y):
        logging.info('"x":{0}, "y":{1}, "event_t":0'.format(x, y))
        
    def on_click(self, x, y, button, pressed):
        if pressed:
            logging.info('"x":{0},"y":{1}, "event_t":1, "button_t":"{2}"'.format(x, y, str(button)))
    
    
    def on_scroll(self, x, y, dx, dy):
        logging.info('"x":{0},"y":{1}, "event_t":3, "x_scroll":{2}, "y_scroll":{3}'.format(x, y, dx, dy))

    def on_press(self, key):
        if key == Key.esc:
            # Stop listeners
            return False
        logging.info('"event_t":4, "key":{0}'.format(key))
    
    def run(self):
        with MouseListener(on_move=self.on_move, 
                    on_click=self.on_click, 
                    on_scroll=self.on_scroll) as m_listener,\
            KeyboardListener(on_press=self.on_press) as k_listner:
            k_listner.join()
            m_listener.join()

