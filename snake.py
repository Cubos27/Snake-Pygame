import pygame


class Snake():
    def __init__(self):
        super().__init__()
        self.snakeBody = [
            [160, 160],
            [145, 145],
            [130, 130],
            [115, 115],
            [100, 100],
        ]
        self.speedX = 5
        self.speedY = 5

    def drawSnake(self):
        for ball in self.snakeBody:
            pygame.draw.circle(screen, "blue", (ball), 15)

    def snakeMovement(self):
        for i in range(1, len(self.snakeBody), 1):
            self.snakeBody[i][1] = self.snakeBody[i-1][0]-10
            self.snakeBody[i][0] = self.snakeBody[i-1][1]-10
        # if (self.speedY <= 0):
        #     for i in range(1, len(self.snakeBody), 1):
        #         self.snakeBody[i][0] = self.snakeBody[i-1][1] + 12
        # else:
        #     for i in range(1, len(self.snakeBody), 1):
        #         self.snakeBody[i][0] = self.snakeBody[i-1][1] - 12

        # if (self.speedX <= 0):
        #     for i in range(1, len(self.snakeBody), 1):
        #         self.snakeBody[i][0] = self.snakeBody[i-1][0] + 12
        # else:
        #     for i in range(1, len(self.snakeBody), 1):
        #         self.snakeBody[i][1] = self.snakeBody[i-1][0] - 12

        self.snakeBody[0][0] += self.speedX
        self.snakeBody[0][1] += self.speedY

    def snakeBounces(self):
        if (self.snakeBody[0][0] <= 0):
            self.speedX *= -1
        if (self.snakeBody[0][0] >= 500):
            self.speedX *= -1
        if (self.snakeBody[0][1] <= 0):
            self.speedY *= -1
        if (self.snakeBody[0][1] >= 400):
            self.speedY *= -1
            # for i in range(len(self.snakeBody)-1, 0, -1):
            #     self.snakeBody.pop(i)
            #     self.snakeBody.append([self.snakeBody[i-1][0] - 12,
            #                            self.snakeBody[i-1][1] + 12])
            #     print(self.snakeBody)

    def updateSnake(self):
        self.drawSnake()
        self.snakeMovement()
        self.snakeBounces()
        print(self.snakeBody)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
running = True

snake = Snake()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    snake.updateSnake()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
