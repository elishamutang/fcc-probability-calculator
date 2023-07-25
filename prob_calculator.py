import copy
import random

class Hat:

    def __init__(self, **kwargs): 
        self.contents = []
        for k,v in kwargs.items():
            for color in range(0, v):
                self.contents.append(k)

    def draw(self, balls_drawn):
        self.balls_drawn = int(balls_drawn)
        if self.balls_drawn <= len(self.contents):
            self.sample_list = random.sample(self.contents, k=balls_drawn)
            for ball in self.sample_list:
                self.contents.remove(ball)
            return self.sample_list
        else:
            return self.contents
        
    def __str__(self):
        return f"{self.contents}"

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0 #how many times you get at least two red balls and one green ball
    N = num_experiments
    balls_expect = Hat(**expected_balls) #Unpack dictionary using ** to pass into Hat class.

    start = copy.deepcopy(hat.contents)
    experiment_draw = hat.draw(num_balls_drawn)
    print(experiment_draw)

    
    

    
    return

