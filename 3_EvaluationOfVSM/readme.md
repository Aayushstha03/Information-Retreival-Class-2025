
# Lab 3: Evaluation of Vector Space Model (VSM)

This lab demonstrates the implementation and evaluation of the Vector Space Model (VSM) for information retrieval:

## 1. Document Representation
- **TF-IDF Vectors:**
	Each document and query is tokenized and represented as a vector of term weights using Term Frequency-Inverse Document Frequency (TF-IDF).

## 2. Similarity Computation
- **Cosine Similarity:**
	Computes the cosine similarity between the query vector and each document vector to rank documents by relevance.

## 3. Ranking
- Documents are sorted in descending order of cosine similarity scores to produce a ranked list of results for the query.

## 4. Evaluation Metrics
- **Precision, Recall, and F1 Score:**
	For each top-k ranked result, the code calculates precision, recall, and F1 score based on a set of relevant documents. This helps assess the effectiveness of the retrieval model.

---

The notebook provides clear code and explanations for each step, offering a practical introduction to VSM-based retrieval and evaluation in IR systems.
