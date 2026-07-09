# 🤖 Robot Simulator

A Python-based robot simulator that demonstrates grid-based robot navigation using **Breadth-First Search (BFS)** and **A\*** path planning algorithms.

The project was built to strengthen software engineering fundamentals through a practical robotics-inspired application. It emphasizes clean object-oriented design, modular programming, algorithm implementation, and command-driven interaction while simulating robot navigation on a 2D grid.

---

## ✨ Features

- Interactive command-line interface
- 2D grid-based robot simulation
- Manual robot movement and rotation
- Obstacle placement and collision avoidance
- Boundary validation
- **Breadth-First Search (BFS)** shortest-path planning
- **A\*** heuristic path planning using Manhattan Distance
- Animated path execution
- Command history and status updates
- Interactive mode and command-file execution
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
├── robot.py         # Robot logic and navigation
├── grid.py          # Grid representation and obstacle handling
├── utils.py         # Helper functions
├── data/            # Command and obstacle files
├── README.md
└── .gitignore
```

---

## 🎮 Supported Commands

| Command | Description |
|----------|-------------|
| `MOVE` | Move the robot one step forward |
| `LEFT` | Rotate the robot 90° left |
| `RIGHT` | Rotate the robot 90° right |
| `REPORT` | Display the robot's current position and direction |
| `BFS X Y` | Navigate to `(X, Y)` using **BFS** |
| `A_STAR X Y` | Navigate to `(X, Y)` using **A\*** |
| `EXIT` | Exit the simulator |

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

## 💻 Example Session

```text
> GO 5 4

Finding shortest path using BFS...

Robot moving...

Destination reached.
```

```text
> ASTAR 2 1

Finding shortest path using A*...

Robot moving...

Destination reached.
```

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
- Graphical visualization using Pygame or Tkinter
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
