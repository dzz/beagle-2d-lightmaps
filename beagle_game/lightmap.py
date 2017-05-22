from client.beagle.beagle_api import api as BGL
from itertools import chain

class Lightmap():
    primitive = BGL.primitive.unit_uv_square

    def __init__(self, **kwargs):
        self.shader = BGL.assets.get("beagle-2d-lightmap/shader/lightmap")
        self.t = 0.0
        self.geometry = Lightmap.vec_2_flat(kwargs['geometry'])
        self.shader.bind( { "geometry" : [ self.geometry ], "num_p" : [ len(self.geometry) ] } )
        self.target_buffer = BGL.framebuffer.from_dims(  kwargs['width'], kwargs['height'], filtered = True )
        self.lights = kwargs['lights']

    def vec_2_flat( geometry ):
        return list(chain(*chain(*geometry)))

    def get_lightmap_texture(self):
        return self.target_buffer.get_texture()

    def get_lightmap_framebuffer(self):
        return self.target_buffer

    def compute(self):
        with BGL.context.render_target( self.target_buffer ):
            BGL.context.clear(0.0,0.0,0.0,1.0)
            for light in self.lights:
                with BGL.blendmode.add:
                    Lightmap.primitive.render_shaded( self.shader, 
                        { 
                            "position"       : light["position"],
                            "light_color"    : light["color"]
                        })
        #self.target_buffer.render_processed( BGL.assets.get("beagle-2d/shader/passthru") )
    
