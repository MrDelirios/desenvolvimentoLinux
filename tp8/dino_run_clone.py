import curses
from enum import Enum
import time
import random


class Screen(Enum):
    HOME = 1
    GAME = 2
    DEAD = 3


class Game():
    def __init__(self, stdcr):
        self.stdscr = stdcr
        self.height, self.width = self.stdscr.getmaxyx()
        self.start_y = 0
        self.start_x = 0
        self.current_screen = Screen.HOME
        self.window = curses.newwin(
                self.height,
                self.width,
                self.start_y,
                self.start_x)
        self.window.timeout(60)
        self.character_y = self.height // 2
        self.obj_y = self.height // 2
        self.obj_speed = 3
        self.character_x = self.width // 5
        self.is_jumping = False
        self.jump_height = 15
        self.gravity_speed = 0.1
        self.obstacles = []
        self.score = 0
        self.highscore_path = ".highscore.txt"
        try:
            with open(self.highscore_path, 'r') as file:
                file.close()
        except FileNotFoundError:
            self.set_highscore(0)
            self.highscore = 0
        self.obs_sprites = {
                0: """


  ║║
  ║║
║ ║║
╚═╗║
  ║║
  ║║  ║
  ║╔══╝
  ║║
  ║║
══╩╩══
                """,
                1: """

  ║║     ║║     ║║
  ║║     ║║     ║║
║ ║║   ║ ║║   ║ ║║
╚═╗║   ╚═╗║   ╚═╗║
  ║║     ║║     ║║
  ║║  ║  ║║  ║  ║║  ║
  ║╔══╝  ║╔══╝  ║╔══╝
  ║║     ║║     ║║
  ║║     ║║     ║║
══╩╩═════╩╩═════╩╩══
                """,
                2: """




  ║║
║ ║║
╚═╗║
  ║║  ║
  ║╔══╝
  ║║
══╩╩══
                """,
                3: """





  ║║
║ ║║
╚═╗║  ║
  ║╔══╝
  ║║
══╩╩══
                """,
                4: """


         ║║
         ║║
  ║║   ║ ║║
║ ║║   ╚═╗║     ║║
╚═╗║     ║║   ╚═╗║
  ║║  ║  ║╔══╝  ║║  ║
  ║╔══╝  ║║     ║╔══╝
  ║║     ║║     ║║
══╩╩═════╩╩═════╩╩══
                """}

    def check_within_bounds(self):
        if not (0 <= self.character_x < self.width and 0 <= self.character_y < self.height):
            raise ValueError(f"Character position out of bounds: x={self.character_x}, y={self.character_y}")

    def adjust_to_resize(self):
        new_height, new_width = self.stdscr.getmaxyx()
        if new_height != self.height or new_width != self.width:
            self.height, self.width = new_height, new_width
            self.window = curses.newwin(
                    self.height,
                    self.width,
                    self.start_y, 
                    self.start_x
                    )
            self.character_y = min(self.character_y, self.height - 2)
            self.character_x = min(self.character_x, self.width - 2)

    def draw_char(self):
        self.check_within_bounds()
        char_sprite = """
        __________
       | Θ        |
       |    ______|
       |    |
       |   |
|\\   _/    |-¬
\\ \\_/     |
 \\        /
  \\  __  -
   ||  ||
   lL  lL
        """

        for i, line in enumerate(char_sprite.split("\n")):
            if self.character_y + i < self.height:
                self.window.addstr(self.character_y + i, self.character_x, line)

    def handle_gravity(self):
        if not self.is_jumping and self.character_y < self.height // 2:
            self.character_y += 1

    def jump(self):
        for _ in range(self.jump_height):
            self.character_y -= 1
        self.render_game_screen()
        time.sleep(self.gravity_speed)

        self.is_jumping = False

    def create_obstacle(self):
        obstacle_y = self.obj_y
        obstacle_x = self.width - 2

        if abs(obstacle_x - self.character_x) < 10:
            obstacle_x += 10

        obs_key = random.choice(list(self.obs_sprites.keys()))
        self.obstacles.append([obstacle_y, self.width - 2, obs_key])

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle[1] -= self.obj_speed
        self.obstacles = [obs for obs in self.obstacles if obs[1] > 0]

    def check_collision(self):
        for obstacle in self.obstacles:
            obs_y, obs_x, _ = obstacle
            if obs_y == self.character_y and abs(obs_x - self.character_x) < 3:
                return True
        return False

    def draw_obs(self):
        for obstacle in self.obstacles:
            y, x, obs_key = obstacle
            if y < 0 or y >= self.height or x < 0 or x >= self.width:
                continue

            obs_sprite = self.obs_sprites[obs_key]

            for i, line in enumerate(obs_sprite.splitlines()):
                if y + i == self.character_y and x == self.character_x:
                    continue

                if y + i < self.height:
                    try:
                        self.window.addstr(y + i, x, line)
                    except curses.error:
                        print(f"Erro ao desenhar sprite na linha {y + i}, {x}")

    def render_game_screen(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(1, 2, f"SCORE: {self.score} HI: {self.get_highscore()} | Press 'q' to quit. Press SPACE to jump")
        self.draw_char()
        self.draw_obs()
        self.window.refresh()

    def get_highscore(self):
        file = open(self.highscore_path, "r")
        hi = file.read()
        file.close()
        return hi

    def set_highscore(self, score):
        file = open(".highscore.txt", "w")
        file.write(str(score))
        file.close()

    def show_game_over_screen(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(self.height // 2, self.width // 2 - 5, "GAME OVER!")
        self.window.addstr((self.height // 2) + 1, self.width // 2 - 9, "PRESS Q TO EXIT")
        self.window.addstr((self.height // 2) + 2, self.width // 2 - 9, "PRESS SPACE TO RESTART")
        self.window.refresh()

        while True:
            key = self.window.getch()
            if key == ord('q'):
                return False
            elif key == ord(' '):
                return True

    def show_home_screen(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr((self.height // 2 - 2), self.width // 2 - 5, "!!!WELCOME TO DINO RUN CLONE!!!")
        self.window.addstr((self.height // 2), self. width // 2 - 5, f"CURRENT HIGHSCORE: {self.get_highscore()}")
        self.window.addstr((self.height // 2 + 2), self.width // 2 - 5, "PRESS SPACE TO BEGIN OR Q TO QUIT")
        self.window.refresh()

        while True:
            key = self.window.getch()
            if key == ord('q'):
                return False
            elif key == ord(' '):
                return True


    def run(self):
        self.render_game_screen()
        obstacle_timer = 0
        spawn_time = 20
        self.obj_speed = 3

        if not self.show_home_screen():
            return

        while True:
            self.adjust_to_resize()
            self.handle_gravity()
            self.move_obstacles()

            if self.check_collision():
                self.set_highscore(self.score)
                if self.show_game_over_screen():
                    spawn_time = 20
                    self.score = 0
                    self.obstacles.clear()
                    self.render_game_screen()
                    continue
                else:
                    break

            self.score += 1
            obstacle_timer += 1

            if self.score % 500 == 0:
                self.obj_speed += 1

            if not self.obstacles and obstacle_timer > spawn_time:
                self.create_obstacle()
                obstacle_timer = 0

            self.render_game_screen()
            self.window.timeout(50)
            key = self.window.getch()

            if key == ord('q'):
                break
            elif key == ord(' ') and not self.is_jumping:
                self.is_jumping = True
                self.jump()


def main(stdscr):
    curses.curs_set(0)
    game = Game(stdscr)
    game.run()


if __name__ == "__main__":
    curses.wrapper(main)
