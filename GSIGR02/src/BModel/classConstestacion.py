class Contestacion:
    def __init__(self, review, dueno, contestacion):
        self.review = review
        self.dueno = dueno
        self.contestacion = contestacion

    def __str__(self):
        return self.review.__str__() + ", " + self.dueno.__str__() + ", " + self.contestacion

