import pygame


class Audio():
    def play(self, path: str) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()