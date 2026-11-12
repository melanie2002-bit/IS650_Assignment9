# IS650_Assignment9
This will contain Assignment 9 files.

# Feature name
Difficulty levels

# Purpose
The purpose of this feature is to allow the user to choose a difficulty level.

# Expected behavior
The user can choose between easy, medium, and hard. 
Easy mode has you try to guess a number between 1 and 10.
Medium mode has you try to guess a number between 1 and 15.
Hard mode has you try to guess a number between 1 and 20.

# At least two test cases that would demonstrate how the feature works
In the beginning of the game, the user would choose between easy, medium, or hard. If they choose medium, they would have to guess between 1-15.
In the beginning of the game, the user would choose between easy, medium, or hard. If they choose hard, they would have to guess between 1-20.

# Feature name
Points Feature

# Purpose
The purpose of this feature is to award the user points based on how many guesses they take to guess the right number

# Expected behavior
If a user guesses correctly the first time, they will get 5 points.
If a user guesses within 2-4 tries, they get 3 points.
If a user guesses in 5+ tries, they get 1 point.

# At least two test cases that would demonstrate how the feature works
While the user is playing the game, if the computer's number is 5, and the user guesses the numbers 3 and 4 before guessing 5, they would get 3 points.
While the user is playing the game, if the computer's number is 8, and the user guesses 8 on the first try, they will get 5 points. 

# Feature Development Comparison
On the manual-feature branch, I added a points system. Users are able to earn points based on how many guesses it took them to guess the number correctly. On the ai-feature branch, I added difficulty levels. In the beginning of the game, users are able to select easy mode, medium mode, or hard mode. On the manual-feature branch, brainstormed some ideas of what I could add that wouldn't be too crazy. Once I thought of the points system, I figured I could use my list variable to help count how many guesses and store that in a points variable. On the ai-feature branch, I used Copilot in VS Code. I told Copilot exactly what difficulty levels I wanted and what I wanted the ranges to be. The code that Copilot produce worked correctly on the first run and did not need any corrections. The AI approach gave me much more confidence because the code seemed more sleek and advanced than my manually-created one. 