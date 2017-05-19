from client.beagle.beagle_api import api as BGL

class Lightmap():
    primitive = BGL.primitive.unit_uv_square
    shader = BGL.assets.get("beagle-2d-lightmap/shader/lightmap")

    def __init__(self):
        pass
    
    def render(self):
        Lightmap.primitive.render_shaded( Lightmap.shader, {})
    
