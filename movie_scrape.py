#   movie_scrapes.py
# Scrapes movies from website and writes them to txt file

from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_site = response.text

soup = BeautifulSoup(movies_site, 'html.parser')
movie_num_and_name = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
ordered_movies = movie_num_and_name[::-1]

with open("films_to_watch.txt", mode="w", encoding="utf8") as film_list:
    for film in ordered_movies:
        film_list.write(f"{film}\n")
