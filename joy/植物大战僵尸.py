import pygame
import sys

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("植物大战僵尸")
clock = pygame.time.Clock()


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 128, 0))  # 用绿色填充背景

        # 在这里添加绘制游戏元素的代码，如植物、僵尸等

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game_loop()
