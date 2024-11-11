# Wordle Application and Solver
Academic project with TELECOM Nancy

[The detailed project description in PDF format](./Projet_P2I2_S2_2122_DP.pdf)


## **Project Description**
The goal of this project was, first, to develop a web application for Wordle. Secondly, the objective was to design a Wordle solver compatible with our application.

## **Wordlove Web Application**
* 2 Game Modes: Classic and Peace&Love
* Statistics: Game history and overall performance
* Account creation and friends list

**Quick Start for Wordle**

After cloning, open the first terminal and run:

```bash
cd project2-E8
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 Wordle/app.py
```

## **Wordle Solver**
* Solves for a [dictionary](./Solveur/liste_78k.txt) with 78k words
* Word sizes: 4 to 8 letters

### **Usage Instructions**

1. Enter the word length in the [wsolf.txt](./Solveur/wsolf.txt) file before starting (ensure correct length).
2. Input the number of attempts at the beginning in the command line, followed by the results for the words proposed by the solver. Results should be in the format `xxx`, where:
   - The number of `x` matches the word length.
   - Each `x` can be 0, 1, or 2.
   - `0` represents a letter not in the word, `1` a misplaced letter, and `2` a correctly placed letter.

   Make sure the length is correct. The solver will then suggest another word. In case of an error, press `Ctrl+C`.

### **Quick Start for Solver**

After cloning, open a second terminal and run:

```bash
cd project2-E8/Solveur/src
make solveur_main_test
```
