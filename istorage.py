from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Interface for movie storage classes.
    """

    @abstractmethod
    def list_movies(self):
        """List all movies in storage."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster=None):
        """Add a new movie to storage."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Delete a movie from storage by title."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Update the rating of a movie in storage."""
        pass
