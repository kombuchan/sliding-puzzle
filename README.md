# Sliding Puzzle Solver

This Python application solves any manually shuffled sliding puzzle configuration using depth-first search (DFS), breadth-first search (BFS), and A* search algorithms. It features an interactive GUI built with the Tkinter module, allowing users to shuffle the puzzle manually and trace the calculated solution in real-time.

## Features

- **Interactive GUI**: Shuffle the puzzle and watch the solution being calculated in real-time.
- **Multiple Solving Algorithms**: Includes DFS, BFS, and A* (using Euclidean and Manhattan heuristics).
- **Performance Metrics**: Displays cost, search depth, and runtime for each solution, all within three seconds.

![image](https://github.com/mihikakrishna/sliding-puzzle/assets/76601670/1ddb18f4-1674-4a69-9367-375a34ef1ff1)

## Installation

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

To run the Sliding Puzzle Solver, you will need to install Tkinter. It usually comes pre-installed with Python. If not, you can install it via pip:

```bash
pip install tk
```

## Usage
To start the application, navigate to the project directory in your terminal and run:

```bash
python driver.py
```

This will launch the GUI where you can shuffle the puzzle and select the algorithm to solve it.

## Code Structure
- driver.py: The main file that sets up the GUI and integrates all components.
- solver.py: Contains the logic for solving the puzzle using different search algorithms.
- state.py: Represents the state of the puzzle at any point.
- euclidean.py, DFS.py, BFS.py: Implement the specific search strategies.
