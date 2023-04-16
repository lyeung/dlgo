# dlgo

[Deep learning with the game of Go] (https://www.manning.com/books/deep-learning-and-the-game-of-go)

## Requirements

- PyEnv 2.3+

## Config

Below are one-off instructions to run when setting up your work environment:

Create virtual environment:

> ./create_env.sh

Activate `dlgo`:

> pyenv activate dlgo

Install tools:

> pip install pip-tools
> pip-compile
> pip install -r requirements.txt

Run the following to re-target your development environment:

> pyenv activate dlgo
