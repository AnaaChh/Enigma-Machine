import pygame

class Rotor:

    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    
    def show_rotor(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n=1, forward=True):
        for idx in range(n):
            if forward is True:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]
        

    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n): 
        # rotate the rotor backwards
        self.rotate(n-1, forward=False)  

        # adjust turnover notch in relation with wiring
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch) 
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch-n+1) % 26]      #???????????????
    
    def draw(self, screen, x, y, w, h, font):
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15) 

        for idx in range(26):
            # left side
            letter = self.left[idx]
            letter = font.render(letter, True, "grey")
            textbox = letter.get_rect(center = (x+w/4,y+(idx+1)*h/27))
            if idx == 0: # highlight top letter
                pygame.draw.rect(screen, "#1255A0", textbox, border_radius=5)
            if self.left[idx] == self.notch: # highlight turnover notch
                pygame.draw.rect(screen, "#8C357F", textbox, border_radius=5)
            
            screen.blit(letter, textbox)

            # right side
            letter = self.right[idx]
            letter = font.render(letter, True, "grey")
            textbox = letter.get_rect(center = (x+w*3/4,y+(idx+1)*h/27))
            screen.blit(letter, textbox)