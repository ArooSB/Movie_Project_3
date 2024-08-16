from omdb_api import fetch_movie_details


class MovieApp:
    def __init__(self, storage, api_key):
        self._storage = storage
        self._api_key = api_key

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        print(len(movies), "movies in total")
        for movie, details in movies.items():
            print(f"{movie}: {details['year']} - Rating: {details['rating']}")

    def _command_add_movie(self):
        title = input("Add a movie name: ")
        if title in self._storage.list_movies():
            print("Movie already in the list.")
            return

        # Fetch movie details from the OMDb API
        details = fetch_movie_details(self._api_key, title)
        if details and "Year" in details and "imdbRating" in details:
            year = details["Year"]
            rating = float(details["imdbRating"])
            poster = details.get("Poster", "N/A")
            self._storage.add_movie(title, year, rating, poster)
            print(f"Movie '{title}' added successfully.")
        else:
            print(f"Could not fetch details for '{title}' from OMDb API.")

    def _command_delete_movie(self):
        title = input("Delete a movie: ")
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully.")

    def _command_update_movie(self):
        title = input("Enter the movie name: ")
        if title not in self._storage.list_movies():
            print("Movie not found.")
        else:
            rating = float(input("Enter the new rating: "))
            self._storage.update_movie(title, rating)
            print(f"Rating for '{title}' updated to {rating}.")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        print(f"Statistics for {len(movies)} movies.")
        # You can add more detailed statistics here

    def _generate_website(self):
        print("Website generation is not implemented yet.")

    def run(self):
        while True:
            print(
                "\nSelect an option:\n"
                "0. Exit\n"
                "1. List movies\n"
                "2. Add movie\n"
                "3. Delete movie\n"
                "4. Update movie\n"
                "5. Show statistics\n"
                "6. Generate website"
            )
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                self._generate_website()
            else:
                print("Invalid choice. Please try again.")
