import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path

    def list_movies(self):
        """
        Reads the CSV file and returns a dictionary of movies,
        where each key is a movie title and the value is another dictionary
        containing the 'rating' and 'year'.
        """
        movies = {}
        try:
            with open(self._file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    movies[title] = {
                        "rating": float(row["rating"]),
                        "year": int(row["year"]),
                    }
        except FileNotFoundError:
            pass  # If file doesn't exist, return an empty dictionary
        return movies

    def add_movie(self, title, year, rating, poster=None):
        """
        Adds a movie to the CSV file. If the movie already exists, it will overwrite it.
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating}
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file by title.
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie in the CSV file.
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        """
        Writes the movies dictionary to the CSV file.
        """
        with open(self._file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "year", "rating"])  # Header
            for title, details in movies.items():
                writer.writerow([title, details["year"], details["rating"]])
