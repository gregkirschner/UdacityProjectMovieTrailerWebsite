This repository holds the files for the Udacity Full-Stack Web Developer Project: "Movie Trailer Website." The exercise was to build server-side code to store a list of movies and their information, which could then be displayed on a website.

The file media.py holds the Movie class, which stores the movies' information.

The file entertainment_center.py constructs my six movies into Movie objects. It also calls the fresh_tomatoes.open_movies_page method to build the site based on the movies it was supplied.

The file fresh_tomatoes.py was provided by Udacity to compile the website into a usable format. A couple of minor tweaks were made by me to update the site, including adding the year to display with the movie.

#Generating the website:
In order to generate the website, the file entertainment_center.py should be run. The files media.py and fresh_tomatoes.py should be in the same folder as the file. Running it will create a new fresh_tomatoes.html file that should open automatically.