import pygame
import sys
from dataclasses import dataclass
# Planet class
# dataclass was explained by TA (Nauka) for unit test file in order to test "check_planet" method
@dataclass

class Planet:
    def __init__(self, name, description, x_start, x_end, image):
        self.name = name #initializes the Planet class
        self.description = description
        self.x_start = x_start #initializes the x positioning object
        self.x_end = x_end
        self.image = image
        self.hit = False  # Controls if popup was already shown

    def is_hit(self, x):
        return self.x_start <= x <= self.x_end

    def get_info(self):
        return f"{self.name}: {self.description}"


# Rocket
class Rocket:
    def __init__(self):
        self.reset()

    def reset(self, HEIGHT=300):
        self.x = 0
        self.y = HEIGHT // 2 + 150
        self.speed = 20  # Smaller step = better planet detection accuracy
        self.current_planet = None

    def move_right(self):
        if self.x + self.speed + 50 <= WIDTH:  # 50 is rocket's width
            self.x += self.speed
        else:
            self.x = WIDTH - 50  # Keep it inside the screen
        print(f"Rocket X: {self.x}")

    def draw(self):
        screen.blit(rocket_img, (self.x, self.y)) #draws the rocket onto the screen

    def check_planet(self, planetS, testing=False):
        for planet in planetS:
            if testing:
                self.current_planet = planet
                return planet

            if planet.is_hit(self.x) and not planet.hit:
                planet.hit = True
                self.current_planet = planet
                return planet
        return None

def show_planet_screen(planet):
    showing = True #sets if the second screen shows or not
    font = pygame.font.SysFont(None, 40) #sets font

    planet_image = pygame.image.load(planet.image).convert_alpha() #loads image of planet on second screen
    planet_image = pygame.transform.scale(planet_image, (300, 300)) #scales size of image

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #if the esc key is pressed goes back to original screen
                    showing = False
        screen.fill((0,0,0)) #wipes the screen and fills with black
        name_text = font.render(f"Welcome to {planet.name}!", True, (255,255,255))
        desc_text = font.render(planet.description, True, (150,150,150))
        tip_text = font.render("Press ESC to return", True, (150,150,150)) #writes instructions and descriptions for planets

        screen.blit(name_text, (WIDTH // 4, HEIGHT // 3 + 150))
        screen.blit(desc_text, (WIDTH // 100 - 5, HEIGHT // 3 + 190))
        screen.blit(tip_text, (WIDTH // 4, HEIGHT // 3 + 230))
        screen.blit(planet_image, (WIDTH // 2 - 150, HEIGHT // 2 - 310 ))
        '''puts all of the images and text onto the second screen'''

        pygame.display.update()



if __name__ == "__main__":
    # Setup
    pygame.init()
    WIDTH, HEIGHT = 1280, 655
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rocket Lands on Planets")

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)

    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('LAND', True, color)
    title_font = pygame.font.SysFont('Corbel', 20)

    # Load Images
    background = pygame.image.load("planets.gif").convert_alpha() #sets the image of the game as a screen
    background = pygame.transform.scale(background, (1280, 250))

    title_text = title_font.render('WELCOME TO THE PLANET EXPLORATION GAME!', True, color)
    instruction1_txt = title_font.render('PRESS -> TO MOVE THE ROCKET', True, color)
    instruction2_txt = title_font.render('PRESS R  TO RESET THE ROCKET', True, color)
    instruction3_txt = title_font.render('CLICK  ON  THE LAND BUTTON  TO  START LEARNING', True, color)

    '''loads instructions on how to play the game on the main screen'''

    back_rect = background.get_rect()
    title_rect = title_text.get_rect()
    instruction1_rect = instruction1_txt.get_rect()
    instruction2_rect = instruction2_txt.get_rect()
    instruction3_rect = instruction3_txt.get_rect()

    '''gets the rects of all of the texts and gets a positioning for their arrangement'''

    title_rect.center = (WIDTH // 2, HEIGHT // 4)
    instruction1_rect.center =(WIDTH // 2, HEIGHT // 2 + 210)
    instruction2_rect.center =(WIDTH // 2, HEIGHT // 2 + 240)
    instruction3_rect.center =(WIDTH // 2, HEIGHT // 2 + 270)
    back_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    '''gives the location of all of the text and where it will be placed'''

    screen.blit(background, back_rect)

    rocket_img = pygame.image.load("rocket.png").convert_alpha()
    rocket_img = pygame.transform.scale(rocket_img, (50, 50))
    rocket_img.set_colorkey((255, 255, 255))

    planet_zones = [
        Planet("Venus", "it is the hottest planet in our solar system, rotates backwards, and has many active volcanoes", 240, 280, "venus-mariner-10-pia23791-fig2.jpg"),
        Planet("Mercury", "it is the smallest, and fastest planet in our solar system, and does not orbit in a perfect circle", 340, 380, "Mercury_in_true_color.jpg"),
        Planet("Earth", "contrary to popular belief is not a round planet, being a oblate spheroid, with 4 layers", 440, 480, "The_Earth_seen_from_Apollo_17.jpg"),
        Planet("Mars", "it has a canyon system larger than any of our own, and the largest volcano in the solar system", 540, 560, "Mars_-_August_30_2021_-_Flickr_-_Kevin_M._Gill.png"),
        Planet("Jupiter", "it is the largest planet in our solar system, and is composed mostly of Hydrogen and Helium", 620, 700, "Jupiter.jpg"),
        Planet("Saturn", "It is most known for its rings made of ice and rock particles, and has around 82 moons in all.", 760, 840, "istockphoto-1496413363-612x612.jpg"),
        Planet("Uranus", "it is known for its almost entirely sideways rotation, and blue-green hue due to methane", 900, 960, "Uranus_Voyager2_color_calibrated.png"),
        Planet("Neptune", "The first planet discovered through mathematical predictions, with winds over 2,000 km/h", 1020, 1100, "Neptune_-_Voyager_2_(29347980845)_flatten_crop.jpg"),
    ]
    # Rocket


    # Setup game
    rocket = Rocket()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, back_rect)
        screen.blit(title_text, title_rect)
        screen.blit(instruction1_txt, instruction1_rect)
        screen.blit(instruction2_txt, instruction2_rect)
        screen.blit(instruction3_txt, instruction3_rect)

        '''puts all of the text onto the screen when it is drawn'''


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #Moves the rocket to the right by using the key "right"
                    rocket.move_right()
                elif event.key == pygame.K_r: #Key "R" sets the rocket to the start
                    rocket.reset()
                    for p in planet_zones:
                        p.hit = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if rocket.current_planet and width / 2.37 <= mouse[0] <= width / 2.37 + 140 and height / 1.445 <= mouse[1] <= height / 1.445 + 40:
                    show_planet_screen(rocket.current_planet) #detects if the land button is clicked


        rocket.current_planet = None
        for planet in planet_zones:
            if planet.is_hit(rocket.x): #handles detections of if the rocket is in the same positioning as a planet
                rocket.current_planet = planet
                break
        rocket.draw()

        if rocket.current_planet:

            pygame.draw.rect(screen, color_light, [width / 2.37, height / 1.445, 180, 60]) #draws the land button when a rocket is over a planet
            screen.blit(text, (width / 2.37 + 50, height / 1.445 + 10)) #places text on the land button
        else:
            pygame.draw.rect(screen, (0, 0, 0), [width / 2.37, height / 1.445, 180, 60]) #sets the boundary of where the button is placed

        pygame.display.update() #updates the game to put all of the info on the screen
        clock.tick(30) #sets the movement speed of the rocket

    pygame.quit()
    sys.exit()


