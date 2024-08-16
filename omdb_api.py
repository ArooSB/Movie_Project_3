import requests


def fetch_movie_details(api_key, title):
    """
    Fetches movie details from the OMDb API.

    :param api_key: Your OMDb API key.
    :param title: The title of the movie to search for.
    :return: A dictionary with movie details, or None if the movie is not found.
    """
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
