import copy
import random

class Hat:

    def __init__(self, **kwargs): 
        self.contents = []
        for k,v in kwargs.items():
            for color in range(0, v):
                self.contents.append(k)

    def draw(self, balls_drawn): #Method used to draw/remove balls at random from contents variable
        self.balls_drawn = int(balls_drawn) #Should receive an integer
        if self.balls_drawn <= len(self.contents):
            self.sample_list = random.sample(self.contents, k=balls_drawn)
            for ball in self.sample_list:
                self.contents.remove(ball)
            return self.contents
        else:
            return self.contents
        
    def __str__(self):
        return f"{self.contents}"

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    copied_hat = copy.copy(hat)
    balls = expected_balls
    return balls
