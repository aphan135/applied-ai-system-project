from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
import os

DEFAULT_TASTE_PROFILE: Dict[str, object] = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "target_tempo_bpm": 120,
    "target_valence": 0.8,
    "target_danceability": 0.8,
    "likes_acoustic": False,
}

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored = []
        for song in self.songs:
            score, _ = score_song(user_prefs, song.__dict__)
            scored.append((score, song))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, song.__dict__)
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file as dictionaries with numeric fields converted to numbers."""
    print(f"Loading songs from {csv_path}...")

    resolved_path = csv_path
    if not os.path.exists(resolved_path):
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        resolved_path = os.path.join(repo_root, csv_path)

    if not os.path.exists(resolved_path):
        return []

    with open(resolved_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        songs = []
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user profile and return the score with explanation reasons."""
    score = 0.0
    reasons: List[str] = []

    genre_weight = 2.0
    mood_weight = 1.0
    energy_weight = 2.0

    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += genre_weight
        reasons.append(f"genre matched (+{genre_weight:.1f})")

    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += mood_weight
        reasons.append(f"mood matched (+{mood_weight:.1f})")

    if "target_energy" in user_prefs and "energy" in song:
        target_energy = float(user_prefs["target_energy"])
        song_energy = float(song["energy"])
        energy_similarity = max(0.0, 1.0 - abs(song_energy - target_energy))
        energy_contribution = energy_weight * energy_similarity
        score += energy_contribution
        reasons.append(
            f"energy similarity {energy_similarity:.2f} -> +{energy_contribution:.2f}"
        )

    if user_prefs.get("likes_acoustic") is True and song.get("acousticness", 0.0) >= 0.7:
        score += 0.5
        reasons.append("acoustic preference matched (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k scored songs ranked from highest to lowest compatibility."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No strong matches"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
