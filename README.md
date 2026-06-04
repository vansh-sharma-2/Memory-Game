# Memory Game

A classic card-matching memory game built with Python and Pygame.

## Gameplay

Flip cards to find matching pairs. Match all 16 pairs to win!

## Prerequisites

- Python 3.x
- Pygame

```bash
pip install pygame
```

## Project Structure

```
├── main.py
└── assets/
    ├── background.png
    ├── unknown.png
    ├── book.png
    ├── crown.png
    ├── egg.png
    ├── heart.png
    ├── hat.png
    ├── key.png
    ├── potion.png
    ├── sword.png
    └── treasure.png
```

## Running the Game

```bash
python main.py
```

## How to Play

1. Click a card to flip it
2. Click a second card to reveal it
3. If both cards match, they stay revealed
4. If they don't match, they flip back after a short delay
5. Match all 16 pairs to win!

## Features

- 8 unique tile types, each appearing twice (16 pairs total)
- Randomized card placement each game
- Win screen on completion
