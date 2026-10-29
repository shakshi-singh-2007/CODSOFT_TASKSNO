# Task 4: Movie Recommendation System (Content-Based Filtering)
# Movies with genres similar to the one you like are recommended.
# Similarity is measured with cosine similarity (no external libraries needed).

import math

MOVIES = {
    "3 Idiots":                 ["comedy", "drama"],
    "Dangal":                   ["drama", "sports"],
    "Chak De India":            ["drama", "sports"],
    "Bahubali":                 ["action", "drama", "fantasy"],
    "KGF":                      ["action", "drama"],
    "Dhoom 2":                  ["action", "thriller"],
    "Drishyam":                 ["thriller", "drama"],
    "Andhadhun":                ["thriller", "comedy"],
    "Hera Pheri":               ["comedy"],
    "Golmaal":                  ["comedy", "action"],
    "Kahaani":                  ["thriller", "drama"],
    "Zindagi Na Milegi Dobara": ["comedy", "drama", "adventure"],
    "Koi Mil Gaya":             ["sci-fi", "drama"],
    "Ra.One":                   ["sci-fi", "action"],
    "Tumbbad":                  ["horror", "fantasy"],
}

ALL_GENRES = sorted({g for genres in MOVIES.values() for g in genres})

def to_vector(genres):
    # Turn a genre list into 0/1 values, one per genre
    return [1 if g in genres else 0 for g in ALL_GENRES]

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0

def recommend(liked_movie, top_n=3):
    if liked_movie not in MOVIES:
        return []
    liked_vec = to_vector(MOVIES[liked_movie])
    scores = []
    for title, genres in MOVIES.items():
        if title != liked_movie:
            scores.append((title, cosine(liked_vec, to_vector(genres))))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]

def main():
    print("Available movies:")
    for m in MOVIES:
        print(" -", m)
    name = input("\nWhich movie do you like? ").strip()
    match = next((m for m in MOVIES if m.lower() == name.lower()), None)
    if not match:
        print("Movie not found in the list.")
        return
    print(f"\nIf you liked '{match}', you may also like:")
    for title, score in recommend(match):
        print(f" - {title}  (match: {score * 100:.0f}%)")

if __name__ == "__main__":
    main()
