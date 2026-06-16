"""
This module contains functions to fetch data from various sources, including.

IMDb, Kaggle, and Polti. Each function is responsible for fetching data from a
specific source and can be called independently or together using the main()
function.

Usage:

    $(ACTIVATE_VENV) && python -m netflix.fetch
"""

from .fetch_imdb import main as fetch_imdb
from .fetch_kaggle_netflix import main as fetch_kaggle_netflix
from .fetch_kaggle_tmdb import main as fetch_kaggle_tmdb
from .fetch_polti import main as fetch_polti


def main():
    fetch_imdb()
    fetch_kaggle_netflix()
    fetch_kaggle_tmdb()
    fetch_polti()
