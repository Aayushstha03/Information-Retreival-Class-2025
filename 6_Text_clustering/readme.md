# Text Clustering Lab

This lab covers several key algorithms for clustering and measuring similarity between text documents:

## 1. KMeans Clustering
KMeans is an unsupervised learning algorithm that partitions documents into k clusters based on their feature vectors (e.g., TF-IDF). It iteratively assigns documents to the nearest cluster centroid and updates centroids until convergence. KMeans is efficient and widely used for text clustering.

## 2. KMedoids Clustering
KMedoids is similar to KMeans but uses actual data points (medoids) as cluster centers instead of centroids. It is more robust to noise and outliers. The algorithm minimizes the sum of dissimilarities between points and their medoid, making it suitable for clustering with arbitrary distance metrics.

## 3. Text Shingling and Jaccard Similarity
Text shingling breaks documents into overlapping substrings (shingles) of length k. Jaccard similarity measures the overlap between sets of shingles from two documents, defined as the size of the intersection divided by the size of the union. This technique is useful for detecting near-duplicate documents and measuring text similarity.

---

These algorithms are demonstrated in the notebooks using practical examples. Explore the code to see how clustering and similarity are applied to text data.
