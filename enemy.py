import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image_large = pygame.image.load(
            vehicle_images[random.randint(0, 8)])
        self.image = pygame.transform.scale(self.image_large, (61, 100))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
        self.speed = speed

    def update(self):
        if self.rect.y > 250:
            self.kill()

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
