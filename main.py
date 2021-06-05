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
                win.blit(pause, (self.x-14, self.y-12)) # 2
            else:
                win.blit(play, (self.x-10, self.y-14)) # 1
        else:
            win.blit(self.text, (self.x, self.y))
            if not self.click:
                pygame.draw.rect(win, (32, 33, 36), (self.x, self.y, self.text.get_width(), self.text.get_height()))
    
    def clicked(self, posx, posy):
        if self.type == 'play_pause':
            if self.x-20 <= posx <= self.x + 20 and self.y - 20 <= posy <= self.y + 20:
                return True
        else:
            if self.x <= posx <= self.x + self.text.get_width() and self.y <= posy <= self.y + self.text.get_height():
                self.click = False
                return True
        return False

def draw_window():
    pygame.draw.circle(win, (252,252,252), (width/2, height/2-80), radius)
    pygame.draw.circle(win, (32, 33, 36), (width/2, height/2-80), radius-3)
    play_pause_btn.draw()
    reset_btn.draw()

    # time
    font1 = pygame.font.SysFont('comicsans', 40)

    if second == -1 and minute == 0 and hour == 0 and day == 0:
        time = font1.render(f'0', 1, (138, 180, 248))
    elif second >= 0:
        time = font1.render(f'{second}', 1, (138, 180, 248))
        if minute == 0 and hour == 0 and day == 0:
            time = font1.render(f'{second}', 1, (138, 180, 248))
        elif minute > 0 and hour == 0 and day == 0:
            time = font1.render(f'{minute}:{second}', 1, (138, 180, 248))
        elif hour > 0 and day == 0:
            time = font1.render(f'{hour}:{minute}:{second}', 1, (138, 180, 248))
        elif day > 0:
            time = font1.render(f'{day}:{hour}:{minute}:{second}', 1, (138, 180, 248))

    win.blit(time, (width/2 - time.get_width()/2, height/2-80 - time.get_height()/2))

def main():
    global second, minute, hour, play_pause_btn, reset_btn, day
    play_pause_btn = Button(width/2, height/2+110, (138, 180, 248), 'play_pause')
    reset_btn = Button(width/2-90, height/2+105, (252,252,252), 'reset')
    run = True
    clock = pygame.time.Clock()
    time = 0
    needed_time = 1000 # In milisseconds
    start_counting = False

    # Time
    second = -1
    minute = 0
    hour = 0
    day = 0

    # Seconds explanation
    '''
    The seconds in lines 84 and 131 need to start at -1 because the clock.tick() gets the time between 
    when the program started to run and now, so if I run the stopwatch file and wait more than one second 
    to click the play button the clock.get_rawtime() will add more than 1000 milisseconds to time. This 
    means that time >= needed_time and start_count will evaluate to True and thus it'll add 1 to time. 
    To revert that, I made the seconds start at -1 so when 1 is added it'll be 0 and start as a normal 
    stopwatch.

    To hide this -1 from the stopwatch interface I made a simple if statement at the draw_window() 
    function (line52).
    '''

    while run:
        clock.tick()
        time += clock.get_rawtime()
        win.fill((32, 33, 36))
        draw_window()

        if time >= needed_time and start_counting:
            time = 0
            second += 1
            if second == 60:
                second = 0
                minute += 1
            
            if minute == 60:
                minute = 0
                hour += 1
            
            if hour == 24:
                hour = 0
                day += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                if play_pause_btn.clicked(x, y):
                    if play_pause_btn.click:
                        play_pause_btn.click = False
                    else:
                        play_pause_btn.click = True

                if play_pause_btn.clicked(x, y) and play_pause_btn.click:
                    reset_btn.click = True
                    start_counting = True
                elif play_pause_btn.clicked(x, y) and not play_pause_btn.click:
                    start_counting = False
                elif reset_btn.clicked(x, y):
                    play_pause_btn.click = False
                    start_counting = False
                    second = -1
                    minute = 0
                    hour = 0
        
        pygame.display.update()

main()
