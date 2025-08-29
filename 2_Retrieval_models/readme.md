
# Lab 2: Retrieval Models in Information Retrieval

This lab demonstrates several foundational techniques for document retrieval and ranking:

## 1. Boolean Information Retrieval
- Documents are indexed using a binary term-document matrix.
- Supports Boolean queries (AND, OR, NOT) to retrieve matching documents.

## 2. Term Weighting Mechanisms
- **TF (Term Frequency):** Measures how often a term appears in a document.
- **IDF (Inverse Document Frequency):** Measures how unique a term is across all documents.
- **TF-IDF:** Combines TF and IDF to assign importance to terms for each document.

## 3. Cosine Similarity
- Documents and queries are represented as vectors (Bag of Words or TF-IDF).
- Cosine similarity is computed to measure the closeness between documents and queries.

## 4. KL Divergence Retrieval
- Documents and queries are modeled as probability distributions over the vocabulary.
- KL divergence is used to rank documents by their similarity to the query (lower divergence = more similar).
- Laplace smoothing is applied to avoid zero probabilities.

---

Each technique is implemented with clear code examples and explanations, providing a practical introduction to retrieval models and ranking in IR systems.
