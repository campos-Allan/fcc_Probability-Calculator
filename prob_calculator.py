"""fifth challenge on 'Scientific Computting with Python
on FreeCodeCamp.org
"""
import copy
import random
from typing import Dict, Tuple, List


class Hat:
    """a class representing a hat with balls
    in different colors, each with its quantities
    """

    def __init__(self, **kwargs: Tuple) -> List:
        self.contents = []
        for ball_color, number_of_balls in kwargs.items():
            for num in range(number_of_balls):
                self.contents.append(ball_color)

    def draw(self, number_draws: int) -> List:
        """randomly draw some balls
        from hat

        Args:
            number_draws (int): quantity of balls to be removed

        Returns:
            List: all the balls removed from hat
        """
        if number_draws >= len(self.contents):
            return self.contents

        balls_removed = []
        random_num = 0
        for num in range(number_draws):
            random_num = random.randrange(len(self.contents))
            balls_removed.append(self.contents.pop(random_num))
        return balls_removed


def experiment(hat: object,
               expected_balls: Dict,
               num_balls_drawn: int,
               num_experiments: int) -> float:
    """ number of times a expected set of balls
    comes out of the hat (N), this experiment is repeated a certain
    number (M), the probability then is N/M

    Args:
        hat (object): hat with balls to be removed
        expected_balls (Dict): how many balls are expected from each color
        num_balls_drawn (int): how many balls should be drawn from hat
        in each experiment
        num_experiments (int): number of times the experience should be repeated

    Returns:
        float: probability
    """
    right_combination = 0
    for experiments in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        returned_balls = copy_hat.draw(num_balls_drawn)
        ball_is_found = 0
        for balls, quantities in expected_balls.items():
            if balls in returned_balls:
                if quantities <= returned_balls.count(balls):
                    ball_is_found += 1
        if ball_is_found == len(expected_balls):
            right_combination += 1
    return right_combination/num_experiments
