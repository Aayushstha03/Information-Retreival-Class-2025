# Text Classification Lab - Theory

This lab covers several important techniques for text classification in information retrieval:

## 1. Machine Learning Classifiers

### Naive Bayes
A probabilistic classifier based on Bayes' theorem. It assumes features are independent and calculates the probability of each class given the input text. Naive Bayes is simple, fast, and effective for many text tasks.

### Decision Tree
A tree-based model that splits data based on feature values to classify text. It is interpretable and can handle both categorical and numerical data, but may overfit on small datasets.

### K-Nearest Neighbors (KNN)
A non-parametric method that classifies text based on the majority class among the k closest training samples (neighbors). It relies on a distance metric (often cosine similarity for text) and is simple but can be slow for large datasets.

## 2. Rocchio Algorithm (Relevance Feedback)
The Rocchio algorithm is used for query refinement and relevance feedback. It updates a query vector by moving it closer to relevant documents and away from irrelevant ones, using centroids of each group. This technique improves retrieval and classification by incorporating user feedback.

---

These techniques are demonstrated in the notebooks using toy datasets and practical examples. Explore the code to see how each method works and compare their predictions.