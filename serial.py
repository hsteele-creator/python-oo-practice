"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start = self.next = start
        
    def generate(self):
        """returns start number the first time and adds 1 every call after"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """resets the number for the generate function back to the start number"""
        self.next = self.start
        
