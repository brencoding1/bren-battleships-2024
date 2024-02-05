# Battleships 2024

Battleships 20204 is a game created and ran in the Python terminal. The terminal it's ran in, is the Code Institute mock up terminal in Heroku.

Players can try to beat the game by by finding all of the computers battleships before you run out of chances. Each battleship takes up just one space on the board.

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

[Here is the live version of my project](https://dashboard.heroku.com/apps/bren-battleships-final-final/deploy/github)

<img width="976" alt="Screenshot 2024-02-05 at 07 43 00" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/b37abbf2-e75a-42b0-856e-297dda4076f3">

## How to Play

Battleships 20204 is based on the classic pen and paper game. You can read about more online with a simple Google search.
In this version, you start by entering your board size. This then prompts the machine to generate the battleship board and begin the game with the board size of your choice. You can choose between sizes 1-10. Once this is chosen the board is then displayed. Depending on the size of your board, you then get a number of shots and are told how many ships their are. You are then prompted to enter your column letter, followed by your row number. Once both are selected, it will then mark the board with either an 'X' if you miss, or an 'O' if you hit. You win if you manage to sink all of the battleships before your chances run out.


## Features

### Existing Features

* Homescreen with instructions

The homescreen is where you start off and it explains to you exactly what you have to do.
  
<img width="740" alt="Screenshot 1" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/54e453a4-a865-4e42-8954-504d8286ca17">

* Create your own board size
* Shots left counter
* Ships remaining counter

<img width="740" alt="Screenshot 2" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/40744e3f-a0b1-41ec-b062-f0fdfc5cd128">

* Column selecter
* Row selecter

<img width="285" alt="Screenshot 3" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/d0299b3b-25ca-492b-826a-3549bf153f56">

* Prompt for when you miss

<img width="749" alt="Screenshot 4" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/fb0996aa-8ef4-4c7c-a65e-617197903552">

* Prompt for when you select the wong input

<img width="511" alt="Screenshot 5" src="https://github.com/brencoding1/bren-battleships-2024/assets/107943176/f8a175de-5c0f-4363-a28f-c1bbcbccbf5c">

### Future Features

* Let people play against the computer
* Allow players to position ships themselves
* Allow larger ships that take up more than one space on grid


## Testing

I have manually tested my project by:

* Passing it through a PEP8 linter and confirmed that their are only minor problems with spacing
* Tested in my local terminal and the Code Institute Heroku terminal

Bugs:

Solved Bugs - 

* functions were not working on certan parts because they I decided to change their name in certain places but not in all places, thus leading to system errors

Remaining Bugs:

* No bugs remaining


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku. Below are the steps I followed to be able to deploy the terminal to the website:

Create a new Heroku app on the Heroku website.
Set config vars: Port and give it a value of 8000.
Set buildpacks to Python and NodeJS in that order.
Link the Heroku app to the repository on GitHub.
Click on Deploy.


## Credits

* Code Institute for the deployment terminal.
* Slack searches
* StackOverflow for various problems I faced.
