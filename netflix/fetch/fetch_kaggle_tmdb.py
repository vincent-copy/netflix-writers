"""
Download and prune Kaggle TMDB datasets.

This script downloads Kaggle TMDB's movie metadata dataset, filters it to retain only relevant information,
and exports the results to CSV files.

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
"""

import os

from kaggle.api.kaggle_api_extended import KaggleApi  # type: ignore[import-untyped]

from .const import DB_DIR

KAGGLE_DIR = os.path.join(DB_DIR, "kaggle", "tmdb-movie-metadata")
DATASET = "tmdb/tmdb-movie-metadata"

api = KaggleApi()


def main():
    """
    Download and unzip the Kaggle TMDB movie metadata dataset.

    This function authenticates with the Kaggle API, downloads the specified dataset,
    and unzips it to the designated directory.

    Raises:
        Exception: If there is an error during authentication or dataset download.
    """
    api.authenticate()
    api.dataset_download_files(DATASET, path=KAGGLE_DIR, unzip=True)
    print("Dataset downloaded successfully.")


if __name__ == "__main__":

    main()
