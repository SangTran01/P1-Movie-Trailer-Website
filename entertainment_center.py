import media
import fresh_tomatoes

#creating Movie Objects
toy_story = media.Movie('Toy Story',
                        'A story here',
                        'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

forest_gump = media.Movie('Forest Gump',
                           "A funny man's influences during the 70's- 80's",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=eYSnxZKTZzU")

dark_knight = media.Movie('The Dark Knight',
                          "It's a batman film",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception = media.Movie('Inception',
                        "It's a good sci fi film",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


big_short = media.Movie('The Big Short',
                        "Good movie about the 2008 financial crisis, good times",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/The_Big_Short_teaser_poster.jpg/220px-The_Big_Short_teaser_poster.jpg",
                        "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

guardians = media.Movie('The Guardians of the Galaxy',
                        "Awesome comic book movie",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=2LIQ2-PZBC8")


#combine Movie Objects to movies array
movies = [toy_story, forest_gump, dark_knight, inception, big_short, guardians]

#add movies array to open_movies_page method from fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)


