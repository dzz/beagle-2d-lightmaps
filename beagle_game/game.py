from .lightmap import Lightmap
from random  import uniform
from math import sin,cos
from client.beagle.beagle_api import api as BGL

class game():
    def __init__(self):
        self.t = 0.0

        ### make a bunch of random line segments
        geometry = []
        for i in range(0,16):
            anchor_x = uniform(-0.5,0.5)
            anchor_y = uniform(-0.5,0.5)
            x1 = uniform(-0.5,-0.3)
            x2 = uniform(0.2,0.5)
            y1 = uniform(-0.3,0.5)
            y2 = uniform(-0.5,-0.2)
            if( uniform(0.0,1.0) > 0.5 ):
                x1 = x2
            else:
                y1 = y2

            geometry.append( [ [ x1+anchor_x,  y1+anchor_y ], [ x2+anchor_x,  y2+anchor_y ] ] )
            
        ### make 4 lights
        self.lights = []
        for i in range(0,6):
            self.lights.append( {"color":[ uniform(0.2,1.0),uniform(0.2,1.0),uniform(0.2,1.0),1.0], 
                            "position" : [ uniform(-1.0,1.0), uniform(-1.0,1.0) ] } )

        self.lightmap = Lightmap( geometry = geometry, width = 512, height = 512, lights = self.lights )

    def init(self):
        pass

    def tick(self):
        self.t = self.t +0.01
        for idx, light in enumerate(self.lights):
            light["position"] = [ sin(cos(self.t*3)+idx), sin(cos(self.t+(idx*3))*2) ]
        self.lightmap.compute()

    def render(self):
        self.lightmap.get_lightmap_framebuffer().render_processed( BGL.assets.get("beagle-2d/shader/passthru") )

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
