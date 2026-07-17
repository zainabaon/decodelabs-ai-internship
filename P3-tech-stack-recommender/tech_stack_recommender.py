"""A beginner-friendly content-based tech career recommender.

This program uses TF-IDF and cosine similarity only. It does not use
collaborative filtering or neural networks.
"""

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_FILE = Path(__file__).with_name("raw_skills.csv")
TOP_RECOMMENDATIONS = 3


def load_roles(csv_path: Path) -> list[dict[str, str]]:
    """Load the role-to-skills dataset and validate its required columns."""
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        roles = list(csv.DictReader(file))

    required_columns = {"role", "skills"}
    if not roles or not required_columns.issubset(roles[0]):
        raise ValueError("The CSV file must contain 'role' and 'skills' columns.")
    return roles


def recommend_roles(roles: list[dict[str, str]], user_skills: list[str]) -> list[tuple[str, float]]:
    """Return the top matching roles for the supplied skills."""
    if len(user_skills) < 3:
        raise ValueError("Please provide at least three skills.")

    # Ingestion/normalization: turn the user's skill list into one document.
    user_document = ", ".join(skill.strip() for skill in user_skills if skill.strip())
    if not user_document:
        raise ValueError("Please provide at least three non-empty skills.")

    # TF-IDF scoring: learn the vocabulary from role skill documents, then use
    # that same vocabulary to transform the user's skills.
    documents = [role["skills"] for role in roles]
    vectorizer = TfidfVectorizer(stop_words="english")
    role_vectors = vectorizer.fit_transform(documents)
    user_vector = vectorizer.transform([user_document])

    # Compare the user's vector against every role vector with cosine similarity.
    similarity_scores = cosine_similarity(user_vector, role_vectors).flatten()

    # Sorting and filtering: highest matching roles first, then keep only top 3.
    results = [(role["role"], score) for role, score in zip(roles, similarity_scores)]
    return sorted(results, key=lambda item: item[1], reverse=True)[:TOP_RECOMMENDATIONS]


def main() -> None:
    # Test input: replace this list or collect skills with input() if desired.
    user_skills = ["Python", "Cloud", "Automation"]
    roles = load_roles(DATA_FILE)
    recommendations = recommend_roles(roles, user_skills)

    print(f"Top {TOP_RECOMMENDATIONS} Recommended Career Paths for your skills:")
    for rank, (role, similarity_score) in enumerate(recommendations, start=1):
        match_percentage = similarity_score * 100
        print(f"{rank}. {role} — {match_percentage:.0f}% match")


if __name__ == "__main__":
    main()
