# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This recommender will use a content-based approach: it will compare each song in the dataset to a specific user profile and rank songs by how well they match that profile. The system will read an expanded CSV of songs with fields such as genre, mood, energy, tempo_bpm, valence, danceability, and acousticness, then score every song one by one before returning the top $K$ recommendations.

### Planned Data Flow

1. Input: a user profile describing preferred genre, mood, and target values for numeric traits such as energy, tempo, and valence.
2. Process: loop through every song in the CSV, compare its features to the user profile, and calculate a weighted compatibility score.
3. Output: sort all scored songs from highest to lowest and return the top $K$ results as recommendations.

### Example User Profile

For this version, the system will use a concrete example profile:

- Preferred genre: indie pop
- Preferred mood: chill
- Target energy: moderate
- Target tempo: around 110 bpm
- Target valence: positive but not overly upbeat

### Algorithm Recipe

For each song, the recommender will compute a weighted score using the following logic:

- Genre match: highest weight, because it strongly reflects taste.
- Mood match: strong weight, because it captures the emotional tone of the song.
- Energy similarity: moderate weight, since users often prefer songs at a similar intensity level.
- Tempo similarity: moderate weight, to favor songs with a comparable pace.
- Valence similarity: moderate weight, to reflect whether the song feels happy or calm.
- Danceability and acousticness: smaller weights, used as supporting signals.

A simple version of the scoring rule is:

- Genre score: $0.35$
- Mood score: $0.25$
- Energy score: $0.15$
- Tempo score: $0.10$
- Valence score: $0.10$
- Danceability score: $0.03$
- Acousticness score: $0.02$

Each feature is converted into a similarity score between $0$ and $1$, and the final recommendation score is the weighted sum of those values. After all songs are scored, the system sorts them and returns the highest-ranked results.

### Expected Biases

This system may over-prioritize genre and mood, which could cause it to miss strong songs that fit the user’s energy or tempo better than their stated favorite genre. It may also reflect the limitations of a small, handcrafted dataset, so the recommendations could feel narrow or repetitive.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Here is the verified terminal output from the default "pop/happy" profile:

```text
Loading songs from data/songs.csv...
Loaded songs: 10

Top recommendations:

1. Sunrise City
   Score: 4.96
   Why: genre matched (+2.0); mood matched (+1.0); energy similarity 0.98 -> +1.96

2. Gym Hero
   Score: 3.74
   Why: genre matched (+2.0); energy similarity 0.87 -> +1.74

3. Rooftop Lights
   Score: 2.92
   Why: mood matched (+1.0); energy similarity 0.96 -> +1.92

4. Night Drive Loop
   Score: 1.90
   Why: energy similarity 0.95 -> +1.90

5. Storm Runner
   Score: 1.78
   Why: energy similarity 0.89 -> +1.78
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



