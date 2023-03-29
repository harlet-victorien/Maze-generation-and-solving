import pygame as p

class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 1
        self.color = p.Color(200,30,30)

        

    def deplacer(self, dx, dy, labyrinthe):
        nouveau_x = self.x + (dx * self.vitesse)
        nouveau_y = self.y + (dy * self.vitesse)
        if nouveau_x < 0 or nouveau_x >= len(labyrinthe[0]) or nouveau_y < 0 or nouveau_y >= len(labyrinthe):
            return
        if labyrinthe[nouveau_y][nouveau_x] != 1:
            self.x = nouveau_x
            self.y = nouveau_y
    
   