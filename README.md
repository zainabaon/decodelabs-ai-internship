# Tech Stack Recommender

A small content-based recommendation-system exercise. It converts each role's
skill list and a user's skills into shared TF-IDF vectors, then ranks roles with
cosine similarity.

## Run

```powershell
python -m pip install -r requirements.txt
python tech_stack_recommender.py
```

Edit `user_skills` in `main()` to try another list of at least three skills.
