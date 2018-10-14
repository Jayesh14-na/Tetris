class Score:
    def __init__(self):
        self.lines = 0
        self.level = 0
        self.score = 0

    def add_lines(self, lines):
        self.lines += lines
        self.level  = self.lines//10
        if   lines == 1: self.score += 40   * (self.level + 1)
        elif lines == 2: self.score += 100  * (self.level + 1)
        elif lines == 3: self.score += 300  * (self.level + 1)
        elif lines == 4: self.score += 1200 * (self.level + 1)

