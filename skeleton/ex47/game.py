class Room(object):

    def __init__(self, name, description):
        self.name = name
        sef.description = description
        self.paths ={}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_path(self, paths):
        self.paths.update(paths)
