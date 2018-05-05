from Vehicle import Vehicle
import pygame

class Player_Vehicle(Vehicle):
    def __init__(self,pos):
        self.score = 0
        self.start = (400,300)
