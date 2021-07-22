import random

class BirthdayProblem:
    def __init__(self, dice_range, expected_value_limit):
        self.dice_range = dice_range
        self.expected_value_limit = expected_value_limit
        self.expected_value = 0
        self.dice_count = 0
        self.actual_value = 0
        self.combo_count = 0

    def solve(self):
        while(self.expected_value <= self.expected_value_limit):
            self.actual_value = 0
            self.expected_value = 0
            self.dice_count += 1
            self.combo_count = 0
            experiment = [random.randrange(1, self.dice_range, 1) for i in range(self.dice_count)]
            E = [[0 for i in range(len(experiment))] for j in range(len(experiment))]
            for i in range(len(E)):
                for j in range(i+1,len(E[i])):
                    if experiment[i] == experiment[j]:
                        self.actual_value += 1
                    E[i][j] = 1/self.dice_range
                    self.combo_count += 1
                    self.expected_value += E[i][j]
        return self.actual_value, self.dice_count, self.expected_value, self.combo_count
