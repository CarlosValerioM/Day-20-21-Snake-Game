# Snake Game

A simple Snake game implemented using Python's `turtle` library. The game includes a moving snake and food that grows the snake each time it collides with the food. The game ends if the snake collides with itself.

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/23

## License:
MIT License

## Dependencies:
- Python 3.x
- `turtle` (built-in library)

## Description:
This is a simple Snake game written in Python. The player controls the snake using the arrow keys (Up, Down, Left, Right), and the snake moves in the direction it is heading. The goal is to eat food that appears randomly on the screen, which causes the snake to grow in size. The game ends if the snake collides with itself.

The script makes use of two main modules:
- **`game_intelligence.py`**: Contains the logic for the snake's movement and collision detection.
- **`turtle`**: A built-in Python library used to create the graphical interface.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Snake-Game.git
```
Navigate to the project directory:

```bash
cd Snake-Game
```
Run the game script:

```bash
python snake_game.py
```
Use the arrow keys to control the snake:

Up to move up

Down to move down

Left to move left

Right to move right

## How it works:
The snake is initially created with three segments. The player controls the head of the snake, and it moves in the direction of the current heading. The snake grows by one segment each time it collides with food, which is randomly placed on the screen.

If the snake collides with itself, the game ends. The screen is updated every 0.1 seconds, and the snake's position is updated accordingly.

## Example Output:
The game starts with a snake moving and food that the snake needs to eat. As the snake eats the food, it grows longer. The game ends if the snake collides with itself.

## License:
This project is licensed under the MIT License.
