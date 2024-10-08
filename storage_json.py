import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path

    def list_movies(self):
        try:
            with open(self._file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        with open(self._file_path, "w") as file:
            json.dump(movies, file, indent=4)
