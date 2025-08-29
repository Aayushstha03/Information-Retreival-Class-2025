# Text Clustering Lab

This folder contains examples and code for clustering text documents using different algorithms:

## 1. kmeans.ipynb
- Demonstrates text clustering using the KMeans algorithm from scikit-learn.
- Documents are vectorized using TF-IDF, then grouped into clusters.
- Example output shows which document belongs to which cluster.

## 2. kmediods.ipynb
- Shows how to use the KMedoids algorithm for clustering text.
- Uses TF-IDF vectorization and Euclidean distance to compute document similarity.
- Clusters are formed using the `kmedoids` library.

## 3. text-shingling.ipynb
- Explains text similarity using k-shingles and Jaccard similarity.
- Functions to generate shingles and compute similarity between documents.
- Example compares similarity between different text samples.
