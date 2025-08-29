# Recommendation Systems Lab

This folder demonstrates two main approaches to recommendation systems:

## 1. Collaborative Filtering (collaborative_filtering.ipynb)
Collaborative filtering recommends items to a user based on the preferences of other users with similar tastes. It uses a user-item rating matrix and computes user-user similarity (often with cosine similarity). Recommendations are made by finding items liked by similar users that the target user has not yet rated.

- Pros: Captures complex user-item interactions, works well when there is enough user data.
- Cons: Suffers from cold start (new users/items), sparse data issues.

## 2. Content-Based Filtering (content_based.ipynb)
Content-based filtering recommends items by comparing the content (features, descriptions) of items to the user's preferences. For example, books are recommended based on the similarity of their descriptions using TF-IDF and cosine similarity.

- Pros: Works for new items, no need for other users' data, interpretable recommendations.
- Cons: Limited by the quality and type of item features, may not capture collaborative effects.

Both approaches are illustrated with simple examples in the notebooks. Explore them to see how recommendations are generated for users and items.