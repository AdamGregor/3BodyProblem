
RESET = "\033[0m"

class ColorRow():
    def __init__(self, color, row) -> None:
        self.row = row
        self.color = color

    def __iter__(self):
        yield self.color

        for c in self.row:
            yield c

        yield RESET
