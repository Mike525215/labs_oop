class Lab_one:
    c = 1628 % 3
    def __init__(self, a=1, b=1, n=1, m=1):
        self.a = a
        self.b = b
        self.n = n
        self.m = m
        self.s = 0
    def suma(self):
        if self.a == 1:
            self.ka = 0
        else:
            self.ka = self.a - 1
        if self.b == 1:
            self.kb = 0
        else:
            self.kb = self.b - 1
        for q in range(1, self.n + 1):
            self.s1 = 0
            for j in range(1, self.m + 1):
                self.s1 += ((q + j) / (q + self.c))
            self.s += (self.s1 - self.kb)
        return self.s - self.ka
lab_one = Lab_one(5, 3, 4, 6)
print(lab_one.suma())








