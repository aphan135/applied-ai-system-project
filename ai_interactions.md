# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the agent to research how major streaming platforms such as Spotify and YouTube predict what users will love next, and to explain the difference between collaborative filtering and content-based filtering in a simple, structured way.

**Prompts used:**

> Research how major streaming platforms like Spotify and YouTube predict what users will love next. Focus on the difference between collaborative filtering, which uses other users' behavior, and content-based filtering, which uses song or video attributes. Please explain each approach in plain language, give a real-world example for each, and briefly mention why platforms often combine both methods.

**What did the agent generate or change?**

The agent produced a concise summary explaining that streaming platforms use recommendation systems to infer user preferences from behavior and item characteristics. It described collaborative filtering as predicting what a user might like based on patterns from similar users, while content-based filtering recommends items with features similar to what the user already likes, such as genre, tempo, artist, or audio characteristics. It also noted that modern platforms often combine both approaches with hybrid systems to improve accuracy and reduce the weaknesses of each method.

**What did you verify or fix manually?**

I reviewed the explanation for clarity and accuracy and simplified the wording so it fits a beginner-friendly project context. No code changes were required.

**Main data types involved:**

- User interaction data: likes, dislikes, skips, listens, repeat plays, and playlists
- Song or content attributes: genre, artist, album, tempo, mood, acousticness, danceability, and energy
- Relationship data: similarity between users, similarity between songs, and patterns such as "users who liked X also liked Y"

---

## Content-Based Recommender Analysis (SF11)

**What task did you give the agent?**

I attached the dataset file and asked the agent to analyze the available attributes in the songs dataset and suggest which features would be most effective for a simple content-based recommender.

**Prompts used:**

> I attached songs.csv and would like you to analyze the available data. Please identify which columns would be most useful for a simple content-based recommender, explain why each one matters, and suggest a small set of features to use first. Focus on attributes such as genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. Also evaluate whether these features align with how a musical "vibe" is usually defined.

**What did the agent generate or change?**

The agent suggested starting with a compact set of features that capture both genre and emotional tone, such as genre, mood, energy, valence, and tempo_bpm. It explained that these features are strong indicators of a song's vibe because they describe how energetic, positive, and fast-paced a track feels. It also noted that danceability and acousticness could be useful as secondary features depending on the type of recommendation being built.

**What did you verify or fix manually?**

I reviewed the suggestion and agreed that energy, valence, and tempo_bpm are especially useful for describing vibe, while genre and mood provide a more intuitive way to group songs. In my experience, these features align well with how musical vibe is perceived, although human taste can also depend on personal context, artist familiarity, and lyrical content.

---

## Scoring Rule Design (SF12)

**Algorithm recipe:**

The recommender will score each song by comparing its features to the user's preferred values and rewarding songs that are closer to those preferences. A simple version could use:

- A categorical match for genre and mood, where exact matches receive a higher score.
- A closeness score for numerical features such as energy, valence, and tempo_bpm, where songs closer to the user's preferred value receive a higher score.
- A weighted total so that some features matter more than others, such as genre and mood as strong signals, with energy and tempo as supporting signals.

**Prompt used:**

> Help me design a math-based scoring rule for a simple music recommender. I want the score for a numerical feature like energy to reward songs that are closer to the user's preference, not just songs with higher or lower values. Please show me a simple formula, explain how it works, and suggest a way to combine it with categorical features like genre and mood.

**What did the agent generate or change?**

The agent suggested using a similarity-based rule such as a distance score: score = 1 - abs(feature_value - user_preference) / range. This rewards songs whose values are near the user's preferred value and gives a maximum score of 1 when the values match exactly. It also recommended combining this with categorical matches and weighting each feature so the overall score reflects the user's priorities.

**What did you verify or fix manually?**

I verified that this rule is intuitive and suitable for a simple simulator, because it naturally ranks songs by closeness rather than by raw magnitude. I also noted that the range should be based on the minimum and maximum values in the dataset so the score stays between 0 and 1.

**Why both a scoring rule and a ranking rule are needed:**

A scoring rule determines how much a single song matches the user's preferences, while a ranking rule decides how to order many songs once each one has a score. In other words, the scoring rule answers "How good is this song for the user?" and the ranking rule answers "Which songs should appear first in the recommendation list?" Both are needed because a recommender must first evaluate songs individually and then sort them into a useful final recommendation order.

---

## Dataset Expansion (SF13)

**What task did you give the agent?**

I opened the starter songs dataset and asked the agent to help expand it with additional songs that fit the same CSV structure while introducing a wider range of genres and moods.

**Prompts used:**

> I opened songs.csv and reviewed the existing columns: id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. Please generate 5–10 additional songs in valid CSV format that use the same headers. Make sure the new songs represent a diverse range of genres and moods that are not already strongly represented in the starter file, and keep the numeric values realistic on the same scales used in the dataset.

**What did the agent generate or change?**

The agent produced additional CSV rows with new titles, artists, and feature values that broaden the catalog. The suggestions included genres and moods that helped diversify the dataset beyond the initial examples.

**What did you verify or fix manually?**

I reviewed the generated rows to ensure they matched the expected headers and that the feature values stayed within the dataset’s likely ranges. I also checked that the new songs introduced variety without breaking the CSV format.

---

## Taste Profile Critique (SF14)

**What task did you give the agent?**

I asked the agent to critique the proposed user profile and assess whether it would be sufficient to distinguish between very different musical styles such as intense rock and chill lofi.

**Prompts used:**

> I am designing a simple music recommender and I want to define a user taste profile for comparisons. My current profile uses favorite_genre=pop, favorite_mood=happy, target_energy=0.8, target_tempo_bpm=120, and target_valence=0.8. Please critique whether this profile is too narrow or whether it will be able to distinguish clearly between very different styles such as intense rock and chill lofi. Suggest any improvements that would make the profile more expressive.

**What did the agent generate or change?**

The agent explained that the profile is a good starting point, but it may be too narrow because it strongly centers on one style and could make the system overfit to a single mood or energy level. It suggested making the profile more expressive by adding a broader range of preferences or by including a second preference profile for contrasting moods, such as a calm-vs-intense contrast, so the recommender can better separate different styles.

**What did you verify or fix manually?**

I reviewed the critique and agreed that the current profile is useful for a simple starter version, but it would be stronger if it captured a bit more contrast between energetic and calm songs. This would help the system better distinguish between intense rock and chill lofi.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
