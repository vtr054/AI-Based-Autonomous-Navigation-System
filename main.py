import pygame
import sys
from src.utils.config import *
from src.simulation.environment import Environment
from src.core.pathplanner import PathPlanner
from src.core.navigator import Navigator

class AutonomousNavigationApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("AI-Based Autonomous Navigation System")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)

        # Components
        self.env = Environment(ROWS, COLS)
        self.planner = PathPlanner(ROWS, COLS)
        
        # State
        self.start_pos = (5, 5)
        self.goal_pos = (ROWS - 6, COLS - 6)
        self.navigator = Navigator(self.start_pos)
        self.path = []
        
        self.dragging_obstacles = False
        self.simulation_running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    self.dragging_obstacles = True
                    self.toggle_obstacle_at_mouse()
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging_obstacles = False

            if event.type == pygame.MOUSEMOTION:
                if self.dragging_obstacles:
                    self.toggle_obstacle_at_mouse()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Start Simulation
                    self.start_navigation()
                if event.key == pygame.K_r: # Randomize
                    self.env.generate_random_obstacles(0.2)
                    self.path = []
                if event.key == pygame.K_c: # Clear
                    self.env.clear()
                    self.path = []
                if event.key == pygame.K_p: # Plan only
                    self.path = self.planner.find_path(self.env.grid, self.start_pos, self.goal_pos)

    def toggle_obstacle_at_mouse(self):
        mx, my = pygame.mouse.get_pos()
        col = mx // TILE_SIZE
        row = my // TILE_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            self.env.add_obstacle(row, col)

    def start_navigation(self):
        self.path = self.planner.find_path(self.env.grid, self.start_pos, self.goal_pos)
        if self.path:
            self.navigator.reset(self.start_pos)
            self.navigator.set_path(self.path)
            self.simulation_running = True

    def update(self):
        if self.simulation_running:
            finished = self.navigator.update()
            if finished:
                self.simulation_running = False

    def draw(self):
        self.screen.fill(COLOR_BACKGROUND)
        
        # Draw Grid & Obstacles
        for r in range(ROWS):
            for c in range(COLS):
                rect = (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if self.env.grid[r][c] == 1:
                    pygame.draw.rect(self.screen, COLOR_OBSTACLE, rect)
                else:
                    pygame.draw.rect(self.screen, COLOR_GRID, rect, 1)

        # Draw Planed Path
        if self.path:
            for node in self.path:
                rect = (node[1] * TILE_SIZE + 2, node[0] * TILE_SIZE + 2, TILE_SIZE - 4, TILE_SIZE - 4)
                pygame.draw.rect(self.screen, COLOR_PATH, rect)

        # Draw Start / Goal
        pygame.draw.rect(self.screen, COLOR_START, (self.start_pos[1]*TILE_SIZE, self.start_pos[0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.screen, COLOR_END, (self.goal_pos[1]*TILE_SIZE, self.goal_pos[0]*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # Draw Agent
        current_r, current_c = self.navigator.current_pos
        pygame.draw.circle(self.screen, COLOR_AGENT, 
                           (current_c * TILE_SIZE + TILE_SIZE // 2, 
                            current_r * TILE_SIZE + TILE_SIZE // 2), 
                           TILE_SIZE // 2 - 2)

        # UI Text
        self.draw_text(f"Controls: [SPACE] Start | [R] Randomize | [C] Clean | [P] Plan Path", (10, HEIGHT - 30))
        self.draw_text(f"Status: {'Navigating...' if self.simulation_running else 'Idle'}", (10, HEIGHT - 55))

        pygame.display.flip()

    def draw_text(self, text, pos):
        img = self.font.render(text, True, COLOR_TEXT)
        self.screen.blit(img, pos)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = AutonomousNavigationApp()
    app.run()
