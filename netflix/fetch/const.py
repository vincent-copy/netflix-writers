"""Constants for the fetch module."""

import os

HERE = os.path.abspath(os.path.dirname(__file__))
NETFLIX_DIR = os.path.join(HERE, "..")
REPO_ROOT = os.path.join(NETFLIX_DIR, "..")

DB_DIR = os.path.join(NETFLIX_DIR, "db")
DB_FILE = os.path.join(DB_DIR, "imdb.duckdb")
