from math import sin,cos
from client.beagle.beagle_api import api as BGL

class Lightmap():
    primitive = BGL.primitive.unit_uv_square
    shader = BGL.assets.get("beagle-2d-lightmap/shader/lightmap")

    def __init__(self):
        self.t = 0.0
 
    def tick(self):
        self.t = self.t + 0.01

    def render(self):
        Lightmap.primitive.render_shaded( Lightmap.shader, { "position" : [ sin(self.t), cos(self.t) ] })
    
