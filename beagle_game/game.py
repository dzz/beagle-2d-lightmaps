from .lightmap import Lightmap
from random  import uniform

class game():
    def __init__(self):

        geometry = []
        for x in range(0,32):

            anchor_x = uniform(-1.0,1.0)
            anchor_y = uniform(-1.0,1.0)
            
            x1 = uniform(-0.2,0.2)
            x2 = uniform(-0.2,0.2)
            y1 = uniform(-0.2,0.2)
            y2 = uniform(-0.2,0.2)
            geometry.append( [ 
                                [ x1+anchor_x,  y1+anchor_y ],
                                [ x2+anchor_x,  y2+anchor_y ]
                             ] )
            
        self.lightmap = Lightmap( geometry = geometry)

    def init(self):
        pass

    def tick(self):
        self.lightmap.tick()

    def render(self):
        self.lightmap.render()

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
