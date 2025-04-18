import pandas as pd
from typing import List


def load_csv(path):
    return pd.read_csv(path)


def get_target_artist_songs(dset: pd.DataFrame, artist: str, target_cols: List):
    rst = dset[dset["artist"] == artist][target_cols]
    return rst


TARGET_ARTISTS = [
    "Ed Sheeran",
    "Alan Walker",
    "Shawn Mendes",
    "OneRepublic",
    "Maroon 5",
    "Charlie Puth",
    "Dua Lipa",
    "Billie Eilish",
]
MAIN_COLS = ["artist", "song", "text", "Release Date"]
TARGET_COLS1 = [
    "Tempo",
    "Loudness (db)",
    "Danceability",
    "Energy",
    "Acousticness",
    "Instrumentalness",
    "Liveness",
    "Speechiness",
]
TARGET_COLS2 = [
    "Good for Party",
    "Good for Work/Study",
    "Good for Relaxation/Meditation",
    "Good for Running",
    "Good for Driving",
    "Good for Morning Routine",
    "Good for Social Gatherings",
]
