from math import sin,cos
from client.beagle.beagle_api import api as BGL

class Lightmap():
    primitive = BGL.primitive.unit_uv_square
    frame_buffer = BGL.framebuffer.from_screen()
    shader = BGL.assets.get("beagle-2d-lightmap/shader/lightmap")

    def __init__(self):
        self.t = 0.0
 
    def tick(self):
        self.t = self.t + 0.01

    def render(self):
        geometry = [
            -0.5,-0.5,
            0.5,-0.5,
            -0.5,0.5,
            0.5,0.5
        ]
        with BGL.context.render_target( Lightmap.frame_buffer ):
            Lightmap.primitive.render_shaded( Lightmap.shader, 
                { 
                    "position" : [ sin(self.t+( cos(self.t*3)+1)), cos(self.t) ],
                    "geometry" : [ geometry ],
                    "num_p"    : [ len(geometry) ]
                })
        Lightmap.frame_buffer.render_processed( BGL.assets.get("beagle-2d/shader/passthru") )
    
