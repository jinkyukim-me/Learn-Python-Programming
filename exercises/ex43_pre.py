class Map(object):
    s = {
            "A" : "Apple",
            "B" : "Bridge",
            "C" : "Cat"
}
    def __init__(self, start):
        self.start = start
    def play(self):
        print("gogo!!!")

a_map = Map(Map.s['A'])

print(a_map.start)

a_map.play()
