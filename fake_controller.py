class FakeController:
    def __init__(self):
        self.battery = 100
        self.pressed = set()

    def press(self, button):
        self.pressed.add(button)

    def release(self, button):
        self.pressed.discard(button)
    
    def is_pressed(self, button):
        return button in self.pressed

    def drain(self, amount):
        if(amount < 0):
            raise ValueError("Battery cannot be over 100")
        
        result = self.battery - amount
        self.battery = result

        if self.battery < 0:
            self.battery = 0

        return self.battery
    