"""Import for the two pythone files that help runing the Movie trailer website.
   1)fresh_tomatoes-- contains all the html and css needed to implment the page. that will show the website
   2)media-- contains the class to keep my work separted.
   """
import fresh_tomatoes
import media
"""Instant from class Movie with passing the four paramters.
(movie's name,story line,img url,trailer url"""
toy_story = media.Movie("Toy Story",
                        "toys will come to life",
                        "https://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



despicable_me = media.Movie("Despicable me",
                            "minions and evil stuff",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=nVwae09eSpo")


cars = media.Movie("Cars",
                   "Famous car Maqueen",
                   "https://vignette2.wikia.nocookie.net/pixar/images/2/2f/Cars_poster.jpg/revision/latest?cb=20110414135312",
                   "https://www.youtube.com/watch?v=WGByijP0Leo")

finding_nemo = media.Movie("Finding Nemo",
                           "Lost fish Nemo",
                           "https://vignette1.wikia.nocookie.net/disney/images/8/89/Finding_Nemo_-_Poster.jpg/revision/latest?cb=20160317170204",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")


moana = media.Movie("Moana",
                    "Hwaian girl Moana",
                    "https://vignette2.wikia.nocookie.net/disney/images/d/de/Moana_Poster.jpg/revision/latest?cb=20161220132748",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")


frozen = media.Movie("Frozen",
                     "cursed princess",
                     "https://vignette2.wikia.nocookie.net/disney/images/2/27/Frozen_-_Poster.jpg/revision/latest?cb=20141122215852",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

""""creating an array to hold up all of movies """
movies = [toy_story, despicable_me, cars, finding_nemo, moana, frozen]

"""running my website passing the movies list""""
fresh_tomatoes.open_movies_page(movies)



