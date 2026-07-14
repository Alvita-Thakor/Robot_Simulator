# 🤖 Robot Simulator

A Python-based robot simulator that demonstrates grid-based robot navigation using **Breadth-First Search (BFS)** and **A\*** path planning algorithms.

The project was built to strengthen software engineering fundamentals through a practical robotics-inspired application. It emphasizes clean object-oriented design, modular programming, algorithm implementation, and command-driven interaction while simulating robot navigation on a 2D grid.

---

## ✨ Features

- Interactive **Pygame graphical interface**
- 2D grid-based robot simulation with visual rendering
- Click-to-place obstacles
- Keyboard-based robot movement and rotation
- Click-to-select destination for pathfinding
- Boundary validation
- **Breadth-First Search (BFS)** shortest-path planning
- **A\*** heuristic path planning using Manhattan Distance
- Animated path execution
- Modular object-oriented architecture
- Input validation and error handling

---

## 🧠 Path Planning Algorithms

### Breadth-First Search (BFS)

- Explores the grid level by level
- Guarantees the shortest path in an unweighted grid
- Suitable for exhaustive shortest-path search

### A* Search

- Uses **Manhattan Distance** as the heuristic
- Prioritizes the most promising nodes
- Typically explores fewer nodes than BFS while still guaranteeing the shortest path on this grid

---

## 📂 Project Structure

```text
Robot_Simulator/
│
├── main.py          # Program entry point
├── pygame_ui.py      # Pygame window, rendering, and input handling
├── robot.py         # Robot logic and navigation
├── grid.py          # Grid representation and obstacle handling
├── direction.py      # Direction enum
├── utils.py         # Helper functions
├── data/            # Obstacle files
├── README.md
└── .gitignore
```

---

## 🎮 Controls

**Obstacle placement window**
| Input | Action |
|----------|-------------|
| Click a cell | Toggle obstacle on/off |
| `ENTER` | Confirm and continue |

**Simulator window**
| Input | Action |
|----------|-------------|
| `↑` / `↓` | Move the robot forward |
| `←` / `→` | Rotate the robot left / right |
| Click a cell | Set destination |
| `B` | Navigate to destination using **BFS** |
| `N` | Navigate to destination using **A\*** |

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Alvita-Thakor/Robot_Simulator.git
```

### Navigate into the project

```bash
cd Robot_Simulator
```

### Run the simulator

```bash
python main.py
```

---

## 💻 How It Works

1. Run `main.py`. You'll be asked whether to load obstacles from a file or place them manually.
2. If placing manually, a window opens — click cells to toggle obstacles, then press `ENTER`.
3. Enter the robot's starting position and facing direction in the terminal.
4. The main simulator window opens with the robot on the grid.
5. Move the robot with the arrow keys, or click a cell to set a destination and press `B` (BFS) or `N` (A*) to watch the robot path there automatically.

---

## 🛠 Concepts Practiced

### Software Engineering

- Object-Oriented Programming (OOP)
- Modular software architecture
- Separation of responsibilities
- Input validation
- Error handling
- Code refactoring
- Git and GitHub workflow

### Algorithms

- Breadth-First Search (BFS)
- A* Search
- Path reconstruction
- Heuristic search

### Data Structures

- Queue
- Priority Queue (Heap)
- Dictionary
- Set
- Generator-based iteration

---

## 🔮 Future Improvements

- ROS2 integration
- Dynamic obstacle handling
- Multiple robot support
- Weighted grids and Dijkstra's algorithm
- Unit testing
- Configuration file support

---

## 📸 Demo

> Screenshots and an animated demonstration will be added soon.

---

## 👩‍💻 Author

**Alvita Thakor**

If you have suggestions or feedback, feel free to open an issue or contribute to the project.
