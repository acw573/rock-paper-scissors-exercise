# rock-paper-scissors-exercise

## Goal

Create an application to play a game of rock-paper-scissors against a computer.

## Setup

### Repo Setup

In GitHub.com, create a new repo project repository for the game.

Then, "clone" it onto your computer. After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Next, use the command-line to create a file in the repo called "game.py", and then place the following contents inside:

```py
# game.py

print("Time to play Rock, Paper, Scissors, Shoot!")
```

### Environment Setup

> Since we will be working in with environment variables, it is required to use a third-party package called "python-dotenv" to read from the ".env" file.

We will then need to create and activate a new project-specific Anaconda virtual environment with the following command-lines:

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

Then, test the Python script from the command-line:

```sh
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, you're ready to move on to project development. If you do, then you can make your first commit. Commits help with version control.

### Processing User Inputs

The application should prompt the user to input an option (i.e. "rock", "paper", or "scissors") via command-line.

### Validating User Inputs

The application should compare the user's selection against the list of valid options (i.e. "rock", "paper", "scissors") to determine whether the user has selected a valid option.

If the selection is invalid, the program should fail and prevent further program execution.

### Simulating Computer Selection

The application should select one of the options (i.e. "rock", "paper", or "scissors") at random, and assign that as the computer player's choice. Use the `choice()` function provided by [the `random` module](/notes/python/modules/random.md) and ensure the valid choices are stored in a ["list" datatype](/notes/python/datatypes/lists.md), and then pass that list to the random choice function.

### Determining the Winner

The application should compare the user's selection to the computer player's selection, and determine which is the winner using the following logic:

  1. Rock beats Scissors
  2. Paper beats Rock
  3. Scissors beats Paper
  4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

### Displaying Results

After determining the winner, the application should display the results to the user if the game ended in a win, loss or tie.

### Customizing the Player Name

Additionally, you must allow the user to configure their own player name by passing an environment variable called "PLAYER_NAME" stored in a local ".env" file. You need to set up this ".env" file in your text editor.

Make sure the "requirements.txt" file contains:

```sh
python-dotenv
```

Once installed, it is necessary to run `pip install -r requirements.txt` in your command-line to install packages before trying to run the program.


