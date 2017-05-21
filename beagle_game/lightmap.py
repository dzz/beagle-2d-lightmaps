from math import sin,cos
from client.beagle.beagle_api import api as BGL
from itertools import chain

class Lightmap():
    primitive = BGL.primitive.unit_uv_square
    frame_buffer = BGL.framebuffer.from_screen()

    def __init__(self, **kwargs):
        self.shader = BGL.assets.get("beagle-2d-lightmap/shader/lightmap")
        self.t = 0.0
        #self.position = kwargs['position']
        self.geometry = Lightmap.vec_2_flat(kwargs['geometry'])
        #self.lights = kwargs['lights']
        self.shader.bind( { "geometry" : [ self.geometry ] } )

    def tick(self):
        self.t = self.t + 0.01

    def vec_2_flat( geometry ):
        return list(chain(*chain(*geometry)))

    def render(self):
        with BGL.context.render_target( Lightmap.frame_buffer ):
            Lightmap.primitive.render_shaded( self.shader, 
                { 
                    "position" : [ sin(self.t+( cos(self.t*3)+1)), cos(self.t) ],
                    "geometry" : [ self.geometry ],
                    "num_p"    : [ len(self.geometry) ]
                })
        Lightmap.frame_buffer.render_processed( BGL.assets.get("beagle-2d/shader/passthru") )
    
