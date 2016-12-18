import media
import fresh_tomatoes

top_1 = media.Movie('Shawshank Redemption',
                        'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
                        'https://www.youtube.com/watch?v=6hB3S9bIaco')


#print(toy_story.storyline)
#toy_story.show_trailer()

top_2 = media.Movie('Indiana Jones',
                        'Indiana searches for his father, a Holy Grail scholar, who has been kidnapped by Nazis.',
                        'https://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg',
                        'https://www.youtube.com/watch?v=a6JB2suJYHM')

#print(indiana.storyline)
#indiana.show_trailer()

movies=[toy_story, indiana]
fresh_tomatoes.open_movies_page(movies)
