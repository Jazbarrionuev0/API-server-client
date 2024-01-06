# RPG Game API

## Client Side

### Overview
This repository contains a simple RPG (Role-Playing Game) implemented with a client-server architecture. The client-side is scripted in Python, while the server-side uses FastAPI.

### Dependencies
- Python 3.x
- requests library

### Usage
1. Execute the client-side script, initiating communication with the RPG server.
2. The script prompts the user to input their character's name.
3. The RPG character is created, and the user can perform actions such as checking status, eating, exploring, engaging in battles, and exiting the game.

### Characters and Enemies
- **Characters**: Created with attributes like name, health (vida), hunger (hambre), abilities, and damage points (daño).
- **Enemies**: Generated randomly from a list of character names. They have attributes like health, power, and a state indicating if they are alive or dead.

### Actions
- **Check Status (estatus)**: Displays the character's life, hunger, and power.
- **Eat (comer)**: Increases hunger and restores health if hunger exceeds a certain threshold.
- **Battle (batalla)**: Initiates a battle against a randomly generated enemy. The outcome is determined by the character's power and the enemy's health and power.
- **Explore (explorar)**: Grants the character a new ability, increasing their damage points.
- **Exit (salir)**: Ends the game, displaying the number of enemies defeated and their names.

### Game Flow
The game continues until the character's health reaches zero or the player chooses to exit. Characters defeated in battle are marked as "dead" on the server, and new enemies are randomly generated.

## Server Side

### Overview
The server-side script, implemented with FastAPI, provides an API for managing characters and their states. It communicates with a remote data source containing character information.

### Dependencies
- FastAPI
- requests library

### Endpoints
- **GET /personajes**: Retrieves a list of characters from an external data source.
- **PUT /personajes/{nombre}**: Updates the state of a character (e.g., marks them as "dead") based on the provided name.

### Setup
1. Run the server-side script to start the FastAPI server.
2. Execute the client-side script to interact with the RPG game.

## License
This project is licensed under the MIT License.
