# # ORB RUNNER --- A Two-Player Pygame Survival Game

Orb Runner is a two-player survival game built with Python and Pygame.
Players control two moving orbs and compete to survive against
dynamically generated obstacles. The project features multiple obstacle
patterns, responsive movement, UI screens, collision physics, and a
structured game-state system.

## Gameplay Overview

Two players compete on the same screen:

-   Player 1 uses W A S D
-   Player 2 uses Arrow Keys
-   Objective: Survive as long as possible while obstacles spawn
-   If a player collides with an obstacle, the other player wins

Score increases over time based on survival duration.

## Core Components and Functions

Below is a breakdown of the main classes and functions that power the
game.

### 1. Player and Obstacle Classes

#### Player1 and Player2

Each player is a pygame.sprite.Sprite that includes:

-   A circular orb drawn using pygame.draw.circle
-   Hitbox generated using pygame.mask
-   Independent movement controls
-   Key methods:
    -   mvmt() for keyboard-based movement
    -   boundary() to restrict movement within screen
    -   update() combining movement and boundary logic

#### Block

Represents individual obstacles.

-   Rectangle sprite
-   Moves with vx and vy velocities
-   Deletes itself when leaving the screen

Used in all obstacle spawn patterns.

### 2. Core Game Functions

#### display_score()

-   Tracks survival time using pygame timers
-   Adjusts score for restarts, intro delay, and instruction delay
-   Renders score on screen
-   Final score is calculated as score // 150

#### initial_screen()

-   Renders intro screen with pulsing circles
-   Displays title, start option, and instructions option
-   Used when game_state is "intro"

#### instructions()

-   Shows instructions page
-   Explains controls for both players
-   Used when game_state is "instr"

#### game_over()

-   Displays winner information
-   Shows final score
-   Offers options to replay or exit
-   Resets player positions, speed, and obstacle groups

### 3. Collision Systems

#### obst_player_collision()

Handles collision detection between players and obstacles.

Uses an inner function:

##### circle_rect_collision(circle_rect, radius, rect)

-   Performs geometric circle-rectangle intersection test
-   Determines which player collided
-   Updates winner flag and final score
-   Returns False on collision, ending gameplay

#### player_player_collision(p1, p2, rad)

Handles collisions between the two player orbs.

-   Detects overlap
-   Pushes players apart
-   Applies simple elastic velocity changes
-   Clamps velocity to maintain gameplay control

### 4. Obstacle Pattern System

#### obst_spawn_pattern()

Generates random obstacle waves using multiple patterns:

-   vertical_sweep
-   cluster
-   alt_bar
-   double_gap
-   side_rain
-   corridor
-   crusher

One pattern is selected at random every few seconds.

## Setup and Requirements

### Installation

Install Pygame:

    pip install pygame

Run the game:

    python game_final.py


## Assets Required

Place the following files in the same directory:

-   BG.png
-   CaviarDreams_Bold.ttf

## Features

-   Two-player gameplay
-   Smooth movement control
-   Intro screen
-   Instruction screen
-   Multiple obstacle patterns
-   Precise collision detection
-   Player-to-player physics
-   Time-based scoring system
-   60 FPS loop
-   Fullscreen display

## Controls

### Player 1

-   W A S D

### Player 2

-   Arrow Keys

### General

-   Space: Start or Restart
-   Enter: Instructions or Exit
