from pynput.mouse import Button

class Converter:

    def __init__(self, str_btn=None):
        self.str_btn = str_btn

class ButtonConverter(Converter):

    def to_button_controller(self):
        """
        return the corresponding button controller from mouse
        by default it'll return Button.left object
        """
        if self.str_btn == "Button.left":
            return Button.left
        elif self.str_btn == "Button.right":
            return Button.right
        elif self.str_btn == "Button.middle":
            return Button.middle
        return Button.left


class KeyConverter(Converter):
    
    pass