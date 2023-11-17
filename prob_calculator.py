import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument is required.")
        
        self.kwargs = kwargs
        self.contents = []

        for key, value in self.kwargs.items():
            while value > 0:
                self.contents.append(key)
                value -= 1

    def draw(self, balls_to_draw: int):
        # Make a deep copy of the hat's contents
        hat_copy = []
        for key, value in self.kwargs.items():
            while value > 0:
                hat_copy.append(key)
                value -= 1  

        total_balls = len(self.contents)
        balls_drawn = []
    
        if balls_to_draw > total_balls:
            # Handle the case where balls_to_draw is greater than or equal to the total number of balls
            return self.contents
        else:

            for i in range(balls_to_draw):
                ball_drawn = random.choice(hat_copy)
                hat_copy.remove(ball_drawn)
                balls_drawn.append(ball_drawn)
        
        self.contents = hat_copy        
        return balls_drawn

def experiment(**kwargs):
    hat = kwargs.get("hat", None)
    expected_balls = kwargs.get("expected_balls", {})   
    num_balls_drawn = kwargs.get("num_balls_drawn", 0) 
    num_experiments = kwargs.get("num_experiments", 1)

    counter = num_experiments
    successful_experiments = 0
    while counter > 0:
        lst_result = hat.draw(num_balls_drawn)
        dic_result = {key: lst_result.count(key) for key in set(lst_result)}

        experiment_successful = True
        for key, value in expected_balls.items():
            if key not in dic_result or dic_result[key] < value:
                experiment_successful = False
                break
        
        if experiment_successful:
            successful_experiments += 1
        
        counter -= 1
    
    return successful_experiments / num_experiments
