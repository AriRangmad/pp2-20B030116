from os import scandir
from select import select
import pygame
import psycopg2

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400

BLOCK_SIZE = 20


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food:
    def __init__(self):
        self.location = Point(4, 10)

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()

    conn = psycopg2.connect(
       host = "localhost",
       database = "postgres",
       user = "postgres",
       password = "qwerty")

    username = input("Enter your user name...")
    new_user = f"insert into snake (user_name, score) values ('{username}', 0);"


    cursor = conn.cursor()
    cursor.execute("select * from snake")
    check = cursor.fetchall()
    if (any(username in i for i in check)) :
        cursor.execute(f"select score from snake where user_name = '{username}';")
        save_sql = f"update snake set score = {snake.score} where user_name = '{username}';"
    else:
        cursor.execute(new_user)
        conn.commit()
        snake.score = 0
        snake.level = 1
    conn.commit() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()

        snake.check_collision(food)

        SCREEN.fill(BLACK)

        
        snake.draw()
        food.draw()
        
        drawGrid()

        pygame.display.update()
        CLOCK.tick(5)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()