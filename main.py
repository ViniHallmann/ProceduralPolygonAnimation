#PROCEDURAL POLYGON ANIMATION
import pygame
import random
import math
import pygame.gfxdraw

#GLOBALS
WIDTH:  int = 1280
HEIGHT: int = 254
FPS:    int = 120
FONT = None

NUMBER_OF_POINTS:   int = 175
DISTANCE_THRESHOLD: int = 60

RADIUS:     list = []
POINTS:     list = []
SPEED:      list = []
COLORS:     list = []

LINE_COLOR:        tuple = (255, 255, 255, 50)
GREY_COLOR:        tuple = (150, 150, 150,50)
BACKGROUND_COLOR:  tuple = (13, 17, 23)

NAME_POSITION:  tuple = WIDTH // 2 - 150, HEIGHT // 2 - 50
TITLE_POSITION: tuple = WIDTH // 2 - 168, HEIGHT // 2

NAME_TEXT:  str = "Vinícius Hallmann"
TITLE_TEXT: str = "Software Developer"

#SETUP FUNCTIONS===================================================================================================
def generate_random_radius():
    for _ in range(NUMBER_OF_POINTS):
        RADIUS.append(random.randint(2, 3))

def generate_random_colors():
    for _ in range(NUMBER_OF_POINTS):
        COLORS.append((random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))

def set_points():
    for _ in range(NUMBER_OF_POINTS):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        POINTS.append((x, y))

def set_speed():
    for _ in range(NUMBER_OF_POINTS):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        SPEED.append((x, y))

def init_font():
    global FONT
    FONT = pygame.font.Font("assets/inter.ttf", 36)

#UPDATE FUNCTIONS==================================================================================================
def update_points():
    for i in range(NUMBER_OF_POINTS):
        x, y = POINTS[i]
        sx, sy = SPEED[i]
        
        #COLISÃO NAS BORDAS
        #"""
        x += sx
        y += sy
        if x <= 0 or x >= WIDTH:
            sx *= -1  
    
        if y <= 0 or y >= HEIGHT:
            sy *= -1  
        
        POINTS[i] = (x, y)
        SPEED[i]  = (sx, sy)
        #"""
        #SEM COLISÃO NAS BORDAS
        """
        x = (x + sx) % WIDTH
        y = (y + sy) % HEIGHT
        POINTS[i] = (x, y)
        """
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_nearest_neighbours(point) -> list:
    neighbours = []
    for p in POINTS:
        if euclidean_distance(point, p) <= DISTANCE_THRESHOLD and p != point:
            neighbours.append(p)
    
    return neighbours

def connect_points(screen):
    for point in POINTS:
        neighbours = get_nearest_neighbours(point)
        for neighbour in neighbours:
            draw_line(screen, point, neighbour, update_color_transparency(euclidean_distance(point, neighbour)))

def update_color_transparency(distance):
    return (255, 255, 255, int(255 - (distance / DISTANCE_THRESHOLD) * 255))

#DRAWING FUNCTIONS=================================================================================================
def draw_line(screen, point, neighbour, color):
    pygame.gfxdraw.line(screen, int(point[0]), int(point[1]), int(neighbour[0]), int(neighbour[1]), color)

def draw_points(screen):
    for i, point in enumerate(POINTS):
        pygame.gfxdraw.filled_circle(screen, int(point[0]), int(point[1]), RADIUS[i], COLORS[i])
        pygame.gfxdraw.aacircle(screen, int(point[0]), int(point[1]), RADIUS[i], COLORS[i])

def draw_title(screen):
    name = FONT.render(NAME_TEXT, True, LINE_COLOR)
    title = FONT.render(TITLE_TEXT, True, GREY_COLOR)

    screen.blit(name, NAME_POSITION)
    screen.blit(title, TITLE_POSITION)

#ANIMATION LOOP====================================================================================================
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Polygon Animation - Vinícius Hallmann")
    clock = pygame.time.Clock()
    running = True
    init_font()
    set_points()
    set_speed()
    generate_random_colors()
    generate_random_radius()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        update_points()
        connect_points(screen)
        draw_points(screen)
        draw_title(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

