# IS211_Assignment9
Week 9 Assignment 9

Author: Moses Permaul - moses.permaul13@spsmail.cuny.edu

Application Details:

1) This web scrapper is setup with 2 files:
	a) football_stats.py
	b) nfl_spreads.py

2) Each file scrapes a different website for football stats

3) The "football_stats.py" file connects to the CBS Sports Touchdown leaders page and returns the top 20 touchdown scorers. 
   Each player's name, position, team, and touchdowns scored are displayed.

4) The "nfl_spreads.py" file connects to Football Locks website and returns the current week's NFL game spreads.
   The favorite, underdown, and spread points are displayed. The home team for each game is designated with the prefix "At".
   
   For example, this is the display for the current week.
   
	   NFL Point Spread - Games Left in Current Week
	   --------------------------------------------
		  Favorite     |   Underdog   |    Spread   
	   --------------------------------------------
		At Pittsburgh  |    Miami     |     -14 
	
	The "At" prefixed infront of Pittsburgh means that the game is being played at Pittsburgh's home stadium,

