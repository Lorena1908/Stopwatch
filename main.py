import pygame
pygame.font.init()

width, height = 300, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stopwatch')
radius = 90
pause = pygame.image.load('images/pause_btn.png')
play = pygame.image.load('images/play_btn.png')
font = pygame.font.SysFont('comicsans', 22)

class PlayPauseButton:
    def __init__(self):
        self.color = (138, 180, 248)
        self.paused = True
        self.x, self.y = (width/2, height/2+150)
    
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), 20)
        if self.paused:
            win.blit(play, (self.x-10, self.y-14))
        else:
            win.blit(pause, (self.x-14, self.y-12))
    
    def clicked(self, posx, posy):
        if self.x-20 <= posx <= self.x + 20 and self.y - 20 <= posy <= self.y + 20:
            if self.paused:
                self.paused = False
            else:
                self.paused = True
            return True
        else:
            return False

# class ResetButton:
#     def __init__(self):
#         self.x, self.y = (width/2-110, height/2+145)
#         self.click = False
#         self.text = font.render('Reset', 1, (252,252,252))
    
#     def draw(self):
#         if not self.click:
#             win.blit(self.text, (self.x, self.y))
#         else:
#             pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.text.get_width(), self.text.get_height()))

def draw_window(play_pause_btn):
    pygame.draw.circle(win, (252,252,252), (width/2, height/2-80), radius)
    pygame.draw.circle(win, (32, 33, 36), (width/2, height/2-80), radius-3)
    play_pause_btn.draw()
    pygame.display.update()

def main():
    play_pause_btn = PlayPauseButton()
    run = True
    while run:
        win.fill((32, 33, 36))
        draw_window(play_pause_btn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                play_pause_btn.clicked(x, y)
        
        # pygame.display.update()

main()
