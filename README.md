# SpaceBusters

SpaceBusters is a 2D space shooting game built using Python's Pygame library. In this game, the player controls a spaceship and shoots enemies while avoiding enemy bullets. The goal is to achieve the highest score possible by defeating enemies.

## Features

- **Player Control**: Move the player’s spaceship left and right.
- **Shooting Mechanism**: Fire bullets from the player's spaceship to destroy enemy ships.
- **Enemy Ships**: The game includes multiple enemy ships that move on the screen and fire bullets.
- **Score System**: Earn points by destroying enemy ships. Your score is displayed at the bottom of the screen.
- **High Score Tracking**: The game keeps track of your highest score, saving it to a text file.
- **Game Over Screen**: Displays the final score and allows the player to restart the game or quit.
- **Background Music and Sound Effects**: Background music plays during the game, and sound effects play when bullets are fired.

## Installation

To run SpaceBusters, ensure you have Python and Pygame installed. You can install Pygame using the following command:

```bash
pip install pygame
```

## How to Run

1. Clone this repository or download the code files.
2. Place all assets (images, sounds, fonts) in the `assets` folder.
3. Run the `spacebusters.py` file:

```bash
python game.py
```

## Controls

- **Move Left**: Use the left arrow key.
- **Move Right**: Use the right arrow key.
- **Fire Bullet**: Press the `W` key.
- **Restart Game (Game Over Screen)**: Press the `W` key to restart.
- **Quit (Game Over Screen)**: Press `Esc` to quit.

## Game Assets

- **Images**: The game uses various image files such as the player ship, enemies, bullets, and stars. These images are loaded from the `assets` folder.
- **Sounds**: The background music (`bgmusic.mp3`) and the bullet sound effect (`bullet.mp3`) are also loaded from the `assets` folder.
- **Fonts**: Custom fonts are used for displaying the score, title, and instructions.

## How to Play

1. Start the game by pressing the `W` key on the welcome screen.
2. Use the arrow keys to move the spaceship left or right.
3. Press the `W` key to fire bullets at enemy ships.
4. Destroy enemy ships to earn points. Each destroyed enemy gives you 10 points.
5. Avoid enemy bullets! If your spaceship is hit by an enemy bullet, the game is over.
6. On the Game Over screen, check your final score and see if you've beaten the high score. Press `W` to restart or `Esc` to quit.

## High Score

The high score is saved in the `assets/score.txt` file. When you achieve a higher score than the previous one, it will automatically update.

## License

This project is open-source and free to use.