import pygame
import sys
import random

# 初始化 pygame
pygame.init()

# 设置屏幕尺寸和标题
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('贪吃蛇')

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇的初始位置和速度
snake_pos = [100, 50]
snake_speed = [10, 0]

# 蛇的身体
snake_body = [[100, 50], [90, 50], [80, 50]]

# 食物的初始位置
food_pos = [random.randrange(1, screen_width // 10) * 10, random.randrange(1, screen_height // 10) * 10]
food_spawn = True

# 设置游戏速度
clock = pygame.time.Clock()

while True:
    # 检查按键事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed = [0, -10]
            if event.key == pygame.K_DOWN:
                snake_speed = [0, 10]
            if event.key == pygame.K_LEFT:
                snake_speed = [-10, 0]
            if event.key == pygame.K_RIGHT:
                snake_speed = [10, 0]

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新蛇的位置
    snake_pos[0] += snake_speed[0]
    snake_pos[1] += snake_speed[1]

    # 蛇身体增长
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # 生成新的食物
    if not food_spawn:
        food_pos = [random.randrange(1, screen_width // 10) * 10, random.randrange(1, screen_height // 10) * 10]
    food_spawn = True

    # 清空屏幕
    screen.fill(WHITE)

    # 画蛇和食物
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # 更新屏幕
    pygame.display.flip()

    # 检查蛇是否撞到边界或自己
    if snake_pos[0] < 0 or snake_pos[0] > screen_width - 10 or snake_pos[1] < 0 or snake_pos[1] > screen_height - 10:
        pygame.quit()
        sys.exit()
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    # 控制游戏速度
    clock.tick(30)