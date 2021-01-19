import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Chel import Chel


windowSize = 640, 480


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    chel = Chel(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not chel.restart:
        pygame.display.set_caption("Чел запущен с  {:d} FPS".format(int(clock.get_fps())))
        if chel.pause:
            chel.pauseObj.update()
        else:
            level.drawLevel(chel.camera)
            dashboard.update()
            chel.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
