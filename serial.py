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
    def __init__(self, start):
        "Initializes start and inc variables"
        self.start = start
        self.inc = start - 1

    def generate(self):
        "Increases then returns inc variable"
        self.inc += 1
        return self.inc

    def reset(self):
        "Resets inc variable back to start var minus 1"
        self.inc = self.start - 1

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


