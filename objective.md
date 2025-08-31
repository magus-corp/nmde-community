# New feature: Adding a bunch of dockerized applications

I will import an folder called composes. In this folder you will find a bunch of applications and services in docker compose format.
This applications should be standartized:
- All should have the same formatting
- All that need some kinda of database should have the database inside the docker-compose of the target application now exposing ports to the system.
- We will prioritize the minimization of ports of the host but separating the networks.
- We Will create an application like the nmde one in the bin folder to manage what are the docker-composes that are up and what are the ones that are down.
- The application should follow the mnde style and structure. With an x marks the spot kinda of selection list with the sync option at the bottom that launch the ones marked and down the ones not marked. 
- The list should be dynamic. We should provide a template so the user can write their own docker-composes stacks. Adding the to the composes folder should automagicly make them avaliable in the list.
- We need routines that check for port overlap and other type of simple errors
- After launch the visibility and overall manipulation of the applications will be done from the lazydocker application.
- The environment manipulation should be storage and integrated with an kinda of sqlite (or something idk - envs is a open problem in my mind you can sugest a solution think elegant)

# Changes to the project re-strucutring 
- We need to rewrite the entire bin files into python. We are using only textual and rich for the cli/tui abstraction.
- We will add the relevant scripts and integrate them into our nmde application. In somekind of Spellbook
- I was thinking about the ./bin and ./spellbook the bin for the essential scripts for the work of the nmde itself and the spellbook where we put the scripts that are useful but not essencial or part of the function of the system.


## Developpment Loop

1) Evaluate: Always think in what you will do, how you will do it and the conseguences
- Commit-
2) Plan: After thinking, write your plan.
- Commit-
3) Reevaluate: After planing think again. Remember the wisdom of michelangelo and the marble stone:
      Every block of stone has a statue inside it and it is the task of the sculptor to discover it.
      I saw the angel in the marble and carved until I set him free.
  We are chiseling away the raw caos of creation, take your time in the planning because in life and war usually we only need a good or few good strikes.
- Commit-
4) Implement: Do the work with purpuse and with the gods by your side.
- Commit-
5) Reevaluate.
- Commit-
OBS: You always commit.

## Development Operational
We use for versioning:
git add -A .
git commit -m "Commit(put your significant commit here)"
We use for packages:
uv add packages
uv sync


## DONT'S!

You dont try to run the code, the Tester will run and test the code. You only plan and implement the features.
DONT RUN THE CODE
DONT RUN DOCKER COMPOSE OR DOCKER COMMANDS
