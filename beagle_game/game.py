from .lightmap import Lightmap

class game():
    def __init__(self):
        self.lightmap = Lightmap()

    def init(self):
        pass

    def tick(self):
        pass

    def render(self):
        self.lightmap.render()

    def finalize(self):
        pass

    def configure(self, application_ini):
        pass
