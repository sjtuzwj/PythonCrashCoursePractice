from random import choice

class RandomWalk(object):
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.values=[(0,0)]

    def get_step(self):
        direction=choice([1,-1])
        distance=choice([x for x in range(0,9)])
        return direction*distance

    def fill_walk(self):
        while len(self.values)<self.num_points:
            x_step=self.get_step()
            y_step=self.get_step()

            if x_step==0 and y_step==0:
                continue

            next_value=(self.values[-1][0]+x_step,self.values[-1][1]+y_step)

            self.values.append(next_value)

