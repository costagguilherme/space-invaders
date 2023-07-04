import os
import pygame

class Audio:
    def play(self, path: str) -> None:
        pygame.mixer.init()
        file_path = os.path.join("assets", path)  # Constrói o caminho correto para o arquivo
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()