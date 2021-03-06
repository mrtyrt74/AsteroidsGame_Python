HOW TO PLAY
===========

To play the game, open a terminal (or command line window) and type:
python3 .\game.py

Press Enter a click anywhere on the screen to start the game.

You have 3 lives to begin with (displayed at top left).
Each time a rock hits your spaceship, you lose a life.
You have to avoid rocks.

You begin with a 0 score (displayed at top right corner).

You can move around:
- use left and right (or "a" and "d" if you're a gamer) to rotate your spaceship
- use up arrow (or "w") to accelerate.

You can fire missiles using the "space bar".
- When a missile hits a big rock, it breaks
it into two medium sized ones. Your score goes up by 20.
- When a missile hits a medium sized rock, it
breaks it into two small ones. Your score goes up by 50.
- When a missile hits a small rock, it destroys it completely
and your score goes up by 100.

The game gets more difficult for each 20 seconds you survive:
- One more big rock is added to the screen (they were 4 initially)
- The radius of rocks being created gets smaller, meaning that
they will appear closer to your spaceship.


MEETING THE ASSIGNMENT CRITERIA
===============================

1. The screen is 800 x 600 window.
2. Fast reflex is required for this game. Eventually, rocks will be closer
	to the spaceship and the player must be quick and decide which to destroy
	each quickly.
3. The player has 3 lives, which are displayed at the top left corner.
4. The score is displayed in green at the top right corner of the screen.
5. The difficulty increases every 20 seconds (details described above).
6. The game doesn't crash, since there are only certain actions that are monitored
	from the player.
7. The game has 4 different sounds (soundtrack, when player loses a life, when the game is over,
	and when the player fires a missile).
8. The game has a soundtrack being played throughout the game.
9. The game has a welcome screen, which waits until the player hits enter or clicks somewhere.
10. (BONUS) We've tried to keep everything as nice and smooth as possible. You play and decide though.