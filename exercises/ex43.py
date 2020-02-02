# Exercise 43. Basic Object-Oriented Analysis and Design

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

class CentralCorrior(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the nuutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))

class Map(object):
    scenes = {
            'central_corridor' : CentralCorridor(),
            'laser_weapon_armory' : LaserWeaponArmory(),
            'the_bridge' : TheBridge(),
            'escape_bridge' : TheBridge(),
            'deatth' : Death(),
            'finished' : Finished(),
}
def __init__(self, start_scene):
    self.start_scene = start_scene
def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val
def opening_scene(self):
    return self.next_scene(self.start_scene)

a_map = Map('central_corrior')
a_game = Engine(a_map)
a_game.play()
