# AI-Based Autonomous Navigation System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Robotics](https://img.shields.io/badge/robotics-navigation-orange.svg)

A professional-grade simulation of an **Autonomous Navigation System** designed to demonstrate the fundamentals of robotics perception, path planning, and dynamic obstacle avoidance. 

## 🚀 Key Features
- **A* Pathfinding:** Implementation of the industry-standard heuristic search algorithm for optimal path calculation.
- **Dynamic Obstacle Handling:** Real-time re-routing and collision avoidance.
- **Interactive Environment:** Use your mouse to draw/erase obstacles and watch the AI adapt instantly.
- **Modern UI:** Sleek, dark-themed visualization using Pygame.

---

## 🏗 System Architecture

The project follows a modular robotics architecture:

1. **Perception Layer:** Monitors the grid state and mouse interactions.
2. **Strategy Layer (Path Planner):** Uses A* to calculate the most efficient route.
3. **Execution Layer (Navigator):** Translates coordinates into sequential movements for the agent.

```mermaid
graph LR
    Input[User/Environment] --> Perception
    Perception --> Strategy[A* Planner]
    Strategy --> Execution[Navigator]
    Execution --> Visualization[Pygame View]
```

---

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **Visualization:** Pygame
- **Mathematics:** NumPy
- **Algorithms:** A* (Heuristic Search)

---

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AI-Navigation-System.git
   cd AI-Navigation-System
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Run
Run the simulation:
```bash
python main.py
```

### Controls:
- **Mouse Left-Click/Drag:** Create Obstacles
- **[SPACE]:** Start/Resume Navigation
- **[R]:** Generate Random Obstacles
- **[C]:** Clear Map
- **[P]:** Just Visualize Planned Path

---

## 📝 Industry Relevance
This project implements the same logical flow used in:
- **AMRs (Autonomous Mobile Robots):** Warehouse navigation.
- **UAVs:** Drone flight path planning.
- **FSD:** Self-driving car trajectory mapping.

---
