import pygame

class Reflector:

    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def draw(self, screen, x, y, w, h, font):
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15) 

        for idx in range(26):
            # left side
            letter = self.left[idx]
            letter = font.render(letter, True, "grey")
            textbox = letter.get_rect(center = (x+w/4,y+(idx+1)*h/27))

            screen.blit(letter, textbox)

            # right side
            letter = self.right[idx]
            letter = font.render(letter, True, "grey")
            textbox = letter.get_rect(center = (x+w*3/4,y+(idx+1)*h/27))
            screen.blit(letter, textbox)