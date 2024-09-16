import random
import pygame


class Snake():
    def __init__(self):
        super().__init__()
        self.snake_body = [
            [100, 150],
            [110, 150],
            [120, 150],
            [130, 150],
            [140, 150],
        ]
        self.speedX = 7
        self.speedY = 0
        self.direction = "right"

    def draw_snake(self):
        for point in self.snake_body:
            pygame.draw.circle(screen, "green", (point), 7)

    def snake_movement(self):
        self.snake_body.pop(0)
        self.snake_body.append([self.snake_body[len(self.snake_body)-1][0] + self.speedX,
                               self.snake_body[len(self.snake_body)-1][1] + self.speedY])

    def move_down(self):
        self.speedX = 0
        self.speedY = 10
        self.direction = "down"

    def move_up(self):
        self.speedX = 0
        self.speedY = -10
        self.direction = "up"

    def move_right(self):
        self.speedX = 10
        self.speedY = 0
        self.direction = "right"

    def move_left(self):
        self.speedX = -10
        self.speedY = 0
        self.direction = "left"

    def snake_collided(self):
        if (self.snake_body[len(self.snake_body)-1][0] <= 5 or
                self.snake_body[len(self.snake_body)-1][0] >= 495 or
                self.snake_body[len(self.snake_body)-1][1] <= 5 or
                self.snake_body[len(self.snake_body)-1][1] >= 495):
            return True
        for i in range(1, len(self.snake_body)-2):
            if (self.snake_body[len(self.snake_body)-1][0] == self.snake_body[i][0] and
                    self.snake_body[len(self.snake_body)-1][1] == self.snake_body[i][1]):
                return True

    def updateSnake(self):
        self.draw_snake()
        self.snake_movement()


class Fruit():
    def __init__(self):
        super().__init__()
        self.posx = random.randint(0, 495)
        self.posy = random.randint(0, 495)

    def draw_fruit(self):
        pygame.draw.circle(screen, "Red", (self.posx, self.posy), 7)

    def collision_snake_fruit(self):
        if (snake.snake_body[len(snake.snake_body)-1][0] <= self.posx+10 and
                snake.snake_body[len(snake.snake_body)-1][0] >= self.posx-10 and
                snake.snake_body[len(snake.snake_body)-1][1] <= self.posy+10 and
                snake.snake_body[len(snake.snake_body)-1][1] >= self.posy-10):
            snake.snake_body.append([snake.snake_body[len(snake.snake_body)-1][0],
                                    snake.snake_body[len(snake.snake_body)-1][1]])
            return True


# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pixel_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
title_surf = pixel_font.render('Snake Game', False, "White")
title_rect = title_surf.get_rect(center=(250, 80))

instruction_surf = pixel_font.render('Press any key to start', False, "White")
instruction_rect = instruction_surf.get_rect(center=(250, 420))

game_active = False
snake = Snake()
fruits = []
for i in range(5):
    fruits.append(Fruit())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.move_down()
                if event.key == pygame.K_UP and snake.direction != "down":
                    snake.move_up()
                if event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.move_right()
                if event.key == pygame.K_LEFT and snake.direction != "right":  # me la pelas
                    snake.move_left()
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True

    if game_active:
        screen.fill("black")
        snake.updateSnake()

        for fruit in fruits:
            fruit.draw_fruit()
            if fruit.collision_snake_fruit():
                fruits.pop(fruits.index(fruit))
                fruits.append(Fruit())

        if snake.snake_collided():
            snake.move_right()
            snake.snake_body = [
                [100, 150],
                [110, 150],
                [120, 150],
                [130, 150],
                [140, 150],
            ]
            fruits = []
            for i in range(5):
                fruits.append(Fruit())
            game_active = False
    else:
        screen.fill("black")
        screen.blit(instruction_surf, instruction_rect)
        screen.blit(title_surf, title_rect)

    pygame.display.flip()
    clock.tick(15)
