import sys
import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
import random
import textwrap
from pygame.math import Vector2
from ports import ports


class Socket(pg.Rect):
    def __init__(self, rect, port):
        super().__init__(rect)
        self.proto = port[0]
        self.port_no = str(port[1])
        self.svc_name = port[2]
        self.hint = port[3]
        self.solved = False

class Source(Socket):
    def __init__(self, x, y, port):
        super().__init__((x, y, 100, 20), port)
        self.fg_color = pg.Color('black')
        self.bg_color = pg.Color('khaki')
        
    def render(self):
        if self.solved:
            self.bg_color = pg.Color('green')
        else:
            self.bg_color = pg.Color('khaki')
        text = font.render(self.port_no + '/' + self.proto, 1, self.fg_color)
        rect = pg.Rect(self.x, self.y, text.get_width(), text.get_height())
        pg.draw.rect(screen, self.bg_color, rect.inflate(20,20))
        screen.blit(text, rect)
        

class Destination(Socket):
    def __init__(self, x, y, port):
        super().__init__((x, y, 100, 20), port)
        self.fg_color = pg.Color('black')
        self.bg_color = pg.Color('Lightgreen')
        self.pad = (len(self.proto) + len(self.port_no) + 2) * ' '
        self.pad_len = len(self.pad)
        

    def render(self):
        text = font.render(self.pad + self.svc_name, 1, self.fg_color)
        rect = pg.Rect(self.x, self.y, text.get_width(), text.get_height())
        rect.left = 400 - (text.get_width())
        pg.draw.rect(screen, self.bg_color, rect.inflate(20,20))
        screen.blit(text, rect)

def setup():
    global hint
    global sources
    global destinations
    hint = ""
    sources = []
    destinations = []

    randoms = random.sample(ports, ROWS)
    idx = [y for y in range(ROWS)]
    random.shuffle(idx)
    y = 0
    for i, port in zip(idx, randoms):
        sources.append(Source(20, 20 + idx[i] * 60, randoms[i]))
        destinations.append(Destination(400, 20 + 60*y, port))
        y +=1

def render_multi_line(text, x, y):
    if not text: return
    global font
    text = "\n".join(textwrap.wrap(text, 50))
    lines = text.splitlines()
    text_height = font.size(lines[0])[1]
    for i, l in enumerate(lines):
        screen.blit(font.render(l, 1, pg.Color('black')), (x, y + text_height*i))


ROWS = 11
pg.init()
screen = pg.display.set_mode((420, 768))
pg.display.set_caption('CEHv11 Service Port Training')
font = pg.font.SysFont('Arial',18)

selected_rect = None # currently selected element while dragging

clock = pg.time.Clock()
running = True

setup()

button = Button(screen, 100, 60 * 12, 200, 35, 
    text="Next", fontSize=40, margin=20, inactiveColour=pg.Color('mediumaquamarine'),
    hoverColour=pg.Color('aquamarine'), pressedColour=pg.Color('darkslategray'), radius=5,
    onClick=setup)

while running:
    clock.tick(60)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for rectangle in sources:
                    if rectangle.collidepoint(event.pos):
                        offset = Vector2(rectangle.topleft) - event.pos
                        if not rectangle.solved:
                            selected_rect = rectangle
                        else:
                            offset = Vector2()
                            selected_rect = None

        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and selected_rect and not selected_rect.solved:
                idx = max(min(selected_rect.y//60, ROWS-1), 0)
                target = destinations[idx]
                if target.port_no == selected_rect.port_no:
                    selected_rect.solved = True
                    selected_rect.top = target.top
                    #selected_rect.right = target.left - 10 #TODO fix font rendering width
                selected_rect = None

        elif event.type == pg.MOUSEMOTION:
            if selected_rect:
                selected_rect.topleft = event.pos + offset
            elif event.pos[0] > 300:
                idx = max(min(event.pos[1]//60, ROWS-1), 0)
                target = destinations[idx]
                if target:
                    hint = destinations[idx].hint
            else:
                hint = ""

    screen.fill(pg.Color('mistyrose'))

    for destination in destinations:
        destination.render()
    for rectangle in sources:
        rectangle.render()

    render_multi_line(hint, 5, 60*11)
    pygame_widgets.update(events)
    pg.display.flip()

pg.quit()
sys.exit()