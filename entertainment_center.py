import media, fresh_tomatoes

""" Constructing list of six movies. The greg_movies list will store the list
of movie objects that will be displayed when the
fresh_tomatoes.open_movies_page() method is called. """


# Construct movies:
rushmore = media.Movie("Rushmore",
                       "An eccentric boy in love with his school, bonds and"
                       " battles with his mentor after developing a crush on a"
                       " teacher.",
                       "https://upload.wikimedia.org/wikipedia/en/4/42/Rushmoreposter.png",  # N0QA
                       "https://www.youtube.com/watch?v=GxCNDpvGyss", "1998",
                       "R")

twenty_eight_days_later = media.Movie("28 Days Later",
                                      "A man awakens to a zombie apocalypse and"
                                      " works together with other survivors to"
                                      " find a way to go on.",
                                      "https://upload.wikimedia.org/wikipedia/en/e/e4/28_days_later.jpg",  # N0QA
                                      "https://www.youtube.com/watch?v=c7ynwAgQlDQ",  #N0QA,
                                      "2002", "R")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "A memory erasing procedure gives a couple"
                               " another chance at love.",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",  #N0QA
                               "https://www.youtube.com/watch?v=quuMv7cGUn0",
                               "2004", "R")

primer = media.Movie("Primer",
                     "A mind-bending time-travel cautionary tale.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_%282004_film_poster%29.jpg",  # N0QA
                     "https://www.youtube.com/watch?v=dfOCp6cW7rQ",
                     "2004", "PG-13")

royal_tenenbaums = media.Movie("The Royal Tenenbaums",
                               "A family of childhood prodigies struggles to"
                               " grow up.",
                               "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",  # N0QA
                               "https://www.youtube.com/watch?v=W5AU78dqBgE",
                               "2001", "R")

vanilla_sky = media.Movie("Vanilla Sky",
                          "After a serious accident, a man learns important"
                          " lessons about love and life, but is it too late?",
                          "https://upload.wikimedia.org/wikipedia/en/9/9b/Vanilla_sky_post.jpg",  # N0QA
                          "https://www.youtube.com/watch?v=k09OX40NLUw",
                          "2001", "R")

# Create movies list
greg_movies = [rushmore, twenty_eight_days_later, eternal_sunshine, primer,
               royal_tenenbaums, vanilla_sky]

# Create website
fresh_tomatoes.open_movies_page(greg_movies)
