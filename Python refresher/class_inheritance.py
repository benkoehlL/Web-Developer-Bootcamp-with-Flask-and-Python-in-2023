class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("{} was disconnected".format(self.name))

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("{} is not connected".format(self.name))
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages

printer1 = Device("Printi", "USB")
print(printer1)
printer1.disconnect()

printer2 = Printer("Printi", "USB", 1000) 
printer2.print(20)

print(printer2)
printer2.disconnect()
printer2.print(20)