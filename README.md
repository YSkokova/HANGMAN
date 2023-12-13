Description
Hangman is a popular, funny, yet very grim game. A cruel computer hides a word from you and you need to guess it, letter by letter. If you fail, you'll be hanged, if you win, you'll survive.

You're probably familiar with the rules; now you can create this game yourself!

Let's take a brief look at what you are going to build in this project. Here is what the gameplay will look like:

In the main menu, players can choose to either play or exit the game;
If players choose to play, the computer picks a word from a list — it will be the answer;
The computer asks players to enter a letter that may or may not be in the word;
If players suggest a letter that does not appear in the word for the first time, It's a miss. A player can miss 8 times before the game is over;
If the letter does occur in the word, the computer notifies the players. If there are letters left to guess, the computer invites the player to go on;
When the entire word is uncovered — it's a victory! The game should calculate the final score and return to the main menu.
This may sound complex, but the project is split into small stages with the hints that will guide you. We guarantee that the final product is replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print with Python. Apply that knowledge to entice your friends to play with an announcement for your game!

Objectives
Ask players for a possible word;
Print You survived! if users guess the word;
Print You lost! if users fail.
Create the following list of words: python, java, swift, javascript;
Program the game to choose a word from the list at random (you can use the random library for that). You can enter more words, but let's stick to these four for now.
As in the previous stage, use the following word list: python, java, swift, javascript;
Once the computer has chosen a word from the list, show its first three letters. Replace the hidden letters with hyphens (-).

Your game should work as follows:

Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print: Input a letter:. If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted;
If the letter doesn't appear in the word, the computer takes one try away – even if a user has already suggested this letter – and prints That letter doesn't appear in the word.;
If the letter does appear in the word but a user has already suggested this letter and it's open, no need to print any messages;
If all attempts are exhausted, the game ends; the program shows a final message (Thanks for playing!). Otherwise, players can continue to input letters;
We continue to stick with the word list from the previous stage: python, java, swift, javascript. It ensures that your program is tested reliably. Don't worry about javascript. Yes, it's longer than 8 characters, but we'll keep it in the list for consistency since we're not done with developing the game yet and for now there is no win or lose.

Players start the game with eight lives. In other words, they can make a mistake only eight times.

When players input a valid letter, uncover it in the word, and carry on;
Print That letter doesn't appear in the word. and reduce the number of attempts if the word doesn't contain the letter, even if this particular letter has already been suggested before;
Print No improvements. and reduce the attempt' counter when players input a letter that has been successfully uncovered before;
When players win, print the uncovered word, You guessed the word! , and the winning message. Each one should be on a new line.

To complete this stage, follow the suggested order of the required checks:

Check whether players enter exactly one letter. If not, print Please, input a single letter.. Remember that when players input nothing or non-letter characters, it shouldn't count as a correct input either;
Make sure that the player entered a lowercase English letter. If not, the program should print Please, enter a lowercase letter from the English alphabet.;
If users enter the same letter twice (doesn't matter whether it appears in the word or not), then the program should output You've already guessed this letter.. Do not decrease the number of attempts in this case;
None of the three errors described above should reduce the number of remaining attempts!
When players win, print You guessed the word <word>!, where <word> should be substituted with the uncovered word, and the winning message. Each one should be on a new line.
The game now starts with the menu where players can choose to either play, see their score, or exit;
Print Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: and show this message again if players input something else;
If players choose play, start the game. When the game is finished (regardless of whether a player wins or not), pop up the menu once again to make the gameplay seamless;
If players choose results, print how many games they won, e.g. You won: 0 times, and how many games they lost, e.g. You lost: 25 times;
If players choose exit, end the game.
