class Navigator:
    def __init__(self, start_pos):
        self.current_pos = start_pos
        self.path = []
        self.path_index = 0
        self.is_moving = False

    def set_path(self, new_path):
        self.path = new_path
        self.path_index = 0
        self.is_moving = True if new_path else False

    def update(self):
        """Moves the agent to the next point in the path."""
        if self.is_moving and self.path_index < len(self.path):
            self.current_pos = self.path[self.path_index]
            self.path_index += 1
            if self.path_index >= len(self.path):
                self.is_moving = False
                return True # Reached Goal
        return False

    def reset(self, pos):
        self.current_pos = pos
        self.path = []
        self.path_index = 0
        self.is_moving = False
