import time

COLORS = {
    "green": "\033[92m",  # Green
    "yellow": "\033[93m",  # Yellow
    "red": "\033[91m",  # Red
    "blue": "\033[94m",  # Blue
    "white": "\033[97m",   # White
    "reset": "\033[0m"
}


class ColorText():
    def __init__(self, text, color):
        self.text = text
        self.color = color

    def __iter__(self):
        if self.color is not None:
            yield self.color

        for c in self.text:
            yield c

        yield COLORS["reset"]

class ColorRow():
    def __init__(self):
        self.row = []

    def t(self, text):
        self.row.append(ColorText(text, None))
        return self

    def red(self, text):
        self.row.append(ColorText(text, COLORS["red"]))
        return self

    def green(self, text):
        self.row.append(ColorText(text, COLORS["green"]))
        return self

    def blue(self, text):
        self.row.append(ColorText(text, COLORS["blue"]))
        return self

    def yellow(self, text):
        self.row.append(ColorText(text, COLORS["yellow"]))
        return self

    def white(self, text):
        self.row.append(ColorText(text, COLORS["white"]))
        return self

    def __iter__(self):
        for w in self.row:
            for c in w:
                yield c

        yield COLORS["reset"]

    def print_typed(self, sleep=None):
        if sleep is None:
            print("aaa")
            sleep = 0.05

        curr_row = []
        for w in self.row:
            for c in w:
                curr_row += c
                print(''.join(curr_row), end="\r"+COLORS["reset"])
                time.sleep(sleep)
        print()

