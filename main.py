import pygame
pygame.font.init()

width, height = 260, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stopwatch')
radius = 70
pause = pygame.image.load('images/pause_btn.png')
play = pygame.image.load('images/play_btn.png')
font = pygame.font.SysFont('comicsans', 22)

class Button:
    def __init__(self, x, y, color, type):
        self.type = type
        self.color = color
        self.click = False
        self.text = font.render('Reset', 1, (252,252,252))
        self.x = x
        self.y = y
    
    def draw(self):
        if self.type == 'play_pause':
            pygame.draw.circle(win, self.color, (self.x, self.y), 20)
            if self.click:
                win.blit(pause, (self.x-14, self.y-12))
            else:
                win.blit(play, (self.x-10, self.y-14))
        else:
            win.blit(self.text, (self.x, self.y))
            if self.click:
                pygame.draw.rect(win, (32, 33, 36), (self.x, self.y, self.text.get_width(), self.text.get_height()))
    
    def clicked(self, posx, posy):
        if self.type == 'play_pause':
            if self.x-20 <= posx <= self.x + 20 and self.y - 20 <= posy <= self.y + 20:
                if self.click:
                    self.click = False
                else:
                    self.click = True
                return True
        else:
            if self.x <= posx <= self.x + self.text.get_width() and self.y <= posy <= self.y + self.text.get_height():
                if self.click:
                    self.click = False
                else:
                    self.click = True
                return True
        return False

def draw_window(play_pause_btn, reset_btn):
    pygame.draw.circle(win, (252,252,252), (width/2, height/2-80), radius)
    pygame.draw.circle(win, (32, 33, 36), (width/2, height/2-80), radius-3)
    play_pause_btn.draw()
    reset_btn.draw()

    # time
    font1 = pygame.font.SysFont('comicsans', 70)
    font2 = pygame.font.SysFont('comicsans', 30)
    seconds = font1.render('0', 1, (138, 180, 248))
    miliseconds = font2.render('00', 1, (138, 180, 248))
    win.blit(seconds, (width/2 - seconds.get_width()/2, height/2-80 - seconds.get_height()/2))
    win.blit(miliseconds, (width/2 - miliseconds.get_width()/2 + miliseconds.get_width() + 5, height/2-80 - miliseconds.get_height()/2 + 7))

    pygame.display.update()

def main():
    play_pause_btn = Button(width/2, height/2+110, (138, 180, 248), 'play_pause')
    reset_btn = Button(width/2-90, height/2+105, (252,252,252), 'reset')
    run = True

    while run:
        win.fill((32, 33, 36))
        draw_window(play_pause_btn, reset_btn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                play_pause_btn.clicked(x, y)
                reset_btn.clicked(x, y)
        
        pygame.display.update()

main()
