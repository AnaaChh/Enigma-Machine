import pygame

def draw(eng, path, screen, width, height, margins, gap, font):
    # base coords
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]
    
    # draw path
    y = [margins["top"] + (signal+1)*h/27 for signal in path]
    x = [width - margins["right"] - w/2] #keyboard
    for idx in [4, 3, 2, 1, 0]: # forward path
        x.append(margins["left"] + idx*(gap+w) + w*3/4)
        x.append(margins["left"] + idx*(gap+w) + w*1/4)
    x.append(margins["left"] + w*3/4) # reflector
    for idx in [1, 2, 3 ,4]: # backward path
        x.append(margins["left"] + idx*(gap+w) + w*1/4)
        x.append(margins["left"] + idx*(gap+w) + w*3/4)
    x.append(width - margins["right"] - w/2) # lampboard

    if len(path) > 0:
        for idx in range(1, 21):
            if idx < 10:
                color = "#2FFF0E"
            elif idx < 12:
                color = "#DDFF1E"
            else:
                color = "#FF1C53"
            start = (x[idx-1], y[idx-1])
            end = (x[idx], y[idx])
            pygame.draw.line(screen, color, start, end, width=5)



    # enigma components
    x = margins["left"]
    y = margins["top"]
    for comp in [eng.re, eng.r1, eng.r2, eng.r3, eng.pb, eng.kb]:
        comp.draw(screen, x, y, w, h, font)
        x += w + gap

    # add names 
    names = ["Reflector", "Rotor 3", "Rotor 2", "Rotor 1", "Plugboard", "Key/Lamp"]
    for idx in range(len(names)):
        x = margins["left"] + w / 2 + idx * (w + gap)
        y = margins["top"] * 0.85

        title = font.render(names[idx], True, "white")
        text_box = title.get_rect(center = (x, y))
        screen.blit(title, text_box)
