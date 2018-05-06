import pygame
import random


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, pos, car_choice_count):
        pygame.sprite.Sprite.__init__(self)
        self.image_large = pygame.image.load(vehicle_images[car_choice_count])
        self.image = pygame.transform.scale(self.image_large,(125,95))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
        self.score = 0
        self.y_speed = 5


image1 = './images/car.png'
image2 = './images/taxi.png'
image3 = './images/Police.png'
image4 = './images/Black_viper.png'
image5 = './images/Mini_van.png'
image6 = './images/truck.png'
image7 = './images/Small_truck.png'
image8 = './images/Audi.png'
image9 = './images/Ambulance.png'

vehicle_images = [image1, image2, image3, image4,
                  image5, image6, image7, image8, image9]
