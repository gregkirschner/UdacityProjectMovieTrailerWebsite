import media, fresh_tomatoes

""" Constructing list of six movies. The greg_movies list will store the list
of movie objects that will be displayed when the
fresh_tomatoes.open_movies_page() method is called. """


#Construct movie #1:
rushmore_story = "An eccentric boy in love with his school, bonds and \
battles with his mentor after developing a crush on a teacher."
rushmore_poster = "https://upload.wikimedia.org/wikipedia/en/4/42/\
Rushmoreposter.png"

rushmore = media.Movie("Rushmore", rushmore_story, rushmore_poster,
                       "https://www.youtube.com/watch?v=GxCNDpvGyss", "1998",
                       "R")

#Construct movie #2:
twenty_eight_days_later_poster = "https://upload.wikimedia.org/wikipedia/en/\
e/e4/28_days_later.jpg"
twenty_eight_days_later_story = "A man awakens to a zombie apocalypse and \
works together with other survivors to find a way to go on."
twenty_eight_days_later_url = "https://www.youtube.com/watch?v=c7ynwAgQlDQ"

twenty_eight_days_later = media.Movie("28 Days Later",
                                      twenty_eight_days_later_story,
                                      twenty_eight_days_later_poster,
                                      twenty_eight_days_later_url, "2002", "R")

#Construct movie #3:
eternal_sunshine_poster = "https://upload.wikimedia.org/wikipedia/en/6/62/\
Eternal_sunshine_of_the_spotless_mind_ver3.jpg"
eternal_sunshine_story = "A memory erasing procedure gives a couple another\
chance at love."

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               eternal_sunshine_story, eternal_sunshine_poster,
                               "https://www.youtube.com/watch?v=quuMv7cGUn0",
                               "2004", "R")

#Construct movie #4:
primer_poster = "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_%282004\
_film_poster%29.jpg"
primer_story = "A mind-bending time travel cautionary tale."

primer = media.Movie("Primer", primer_story, primer_poster,
                     "https://www.youtube.com/watch?v=dfOCp6cW7rQ",
                     "2004", "PG-13")

#Construct movie #5:
royal_tenenbaums_poster = "https://upload.wikimedia.org/wikipedia/en/3/3b/\
The_Tenenbaums.jpg"
royal_tenenbaums_story = "A family of childhood prodigies struggles to grow \
up"

royal_tenenbaums = media.Movie("The Royal Tenenbaums", royal_tenenbaums_story,
                               royal_tenenbaums_poster,
                               "https://www.youtube.com/watch?v=W5AU78dqBgE",
                               "2001", "R")

#Construct movie #6:
vanilla_sky_poster = "https://upload.wikimedia.org/wikipedia/en/9/9b/Vanilla\
_sky_post.jpg"
vanilla_sky_story = "After a serious accident, a man learns important lessons\
about love and life, but is it too late?"

vanilla_sky = media.Movie("Vanilla Sky", vanilla_sky_story, vanilla_sky_poster,
                          "https://www.youtube.com/watch?v=k09OX40NLUw",
                          "2001", "R")

#Create movies list
greg_movies = [rushmore, twenty_eight_days_later, eternal_sunshine, primer,
               royal_tenenbaums, vanilla_sky]

#Create website
fresh_tomatoes.open_movies_page(greg_movies)
