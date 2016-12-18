import media
import fresh_tomatoes

t1 = media.Movie('Shawshank Redemption',
                        'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
                        'https://www.youtube.com/watch?v=6hB3S9bIaco')



t2 = media.Movie('The Godfather',
                        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                        'https://s-media-cache-ak0.pinimg.com/736x/40/b4/21/40b421c7cfe1b3059d5e50d79e968270.jpg',
                        'https://www.youtube.com/watch?v=sY1S34973zA')


movies=[t1, t2]
fresh_tomatoes.open_movies_page(movies)
