import pygame

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

NON_ALPHA_KEYS = ["K_0", "K_1", "K_2", "K_3", "K_4", "K_5", "K_6", "K_7", "K_8", "K_9",
"K_BACKQUOTE", "K_MINUS", "K_EQUALS", "K_LEFTBRACKET", "K_RIGHTBRACKET",
"K_BACKSLASH", "K_SEMICOLON", "K_QUOTE", "K_COMMA", "K_PERIOD", "K_SLASH",
"K_SPACE", "K_RETURN", "K_TAB", "K_BACKSPACE", "K_ESCAPE", "K_INSERT",
"K_DELETE", "K_HOME", "K_END", "K_PAGEUP", "K_PAGEDOWN", "K_LEFT", "K_RIGHT",
"K_UP", "K_DOWN", "K_CAPSLOCK", "K_NUMLOCK", "K_SCROLLLOCK", "K_LSHIFT",
"K_RSHIFT", "K_LCTRL", "K_RCTRL", "K_LALT", "K_RALT", "K_MODE", "K_META",
"K_MENU", "K_CLEAR", "K_PRINTSCREEN", "K_PAUSE", "K_F1", "K_F2", "K_F3",
"K_F4", "K_F5", "K_F6", "K_F7", "K_F8", "K_F9", "K_F10", "K_F11", "K_F12",
"K_F13", "K_F14", "K_F15", "K_KP0", "K_KP1", "K_KP2", "K_KP3", "K_KP4",
"K_KP5", "K_KP6", "K_KP7", "K_KP8", "K_KP9", "K_KP_PERIOD", "K_KP_DIVIDE",
"K_KP_MULTIPLY", "K_KP_MINUS", "K_KP_PLUS", "K_KP_ENTER", "K_KP_EQUALS"]

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma machine")

# init fonts
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global vars
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":200, "bottom":200, "left":100, "right":100}
GAP = 75
INPUT = ""
OUTPUT = ""
PATH = []

# historical configuration of the rotors and reflectors if the M3 Enigma
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard configuration
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# initialize enigma machine
eng = Enigma(B, I, II, III, PB, KB)

# set the rings
eng.set_rings((1, 1, 1))

# set the key
eng.set_key("CAT")


animating = True
while animating:
    # background
    SCREEN.fill('#333333')

    # render input
    text = BOLD.render(INPUT, True, "white")
    textbox = text.get_rect(center = (WIDTH/2, MARGINS["top"]/3))
    SCREEN.blit(text, textbox)


    # render input
    text = MONO.render(OUTPUT, True, "white")
    textbox = text.get_rect(center = (WIDTH/2, MARGINS["top"]/3+30))
    SCREEN.blit(text, textbox)

    # draw Enigma machine
    draw(eng, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)    

    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN and event.key not in NON_ALPHA_KEYS:
            if event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
            elif event.unicode:
                key = event.unicode
                if key.lower() in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT += letter
                    PATH, cipher = eng.encrypt(letter) 
                    OUTPUT += cipher

