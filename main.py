from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson


def main():
    api_key = "b489c489"

    # storage = StorageJson("movies.json")
    storage = StorageCsv("movies.csv")

    movie_app = MovieApp(storage, api_key)
    movie_app.run()


if __name__ == "__main__":
    main()
