# vsm_lab_demo.py
from math import log, sqrt
from collections import Counter
import re

docs = [
    "Information retrieval uses ranking to find relevant documents.",
    "Vector space models represent documents and queries as term vectors.",
    "We compute cosine similarity between TF-IDF vectors for retrieval.",
    "Neural models like BERT also perform document ranking.",
    "Evaluation uses precision, recall, and F measure in IR.",
]
doc_ids = [f"D{i + 1}" for i in range(len(docs))]
query = "vector space retrieval ranking"
relevant_set = {"D2", "D3"}

token_pattern = re.compile(r"[a-zA-Z]+")


def tokenize(text):
    return [t.lower() for t in token_pattern.findall(text)]


tokenized_docs = [tokenize(d) for d in docs]
N = len(docs)

df = Counter()
for terms in tokenized_docs:
    for t in set(terms):
        df[t] += 1

idf = {t: log((N + 1) / (df_t + 1)) + 1 for t, df_t in df.items()}


def tfidf_vector(terms):
    tf = Counter(terms)
    vec = {}
    for t, freq in tf.items():
        if t in idf:
            vec[t] = (freq) * idf[t]
    return vec


def cosine_sim(v1, v2):
    dot = sum(v1.get(t, 0) * v2.get(t, 0) for t in set(v1) | set(v2))
    n1 = sqrt(sum(w * w for w in v1.values()))
    n2 = sqrt(sum(w * w for w in v2.values()))
    if n1 == 0 or n2 == 0:
        return 0.0
    return dot / (n1 * n2)


doc_vectors = [tfidf_vector(tokenize(d)) for d in docs]
query_vec = tfidf_vector(tokenize(query))

scores = [
    (doc_id, cosine_sim(query_vec, vec)) for doc_id, vec in zip(doc_ids, doc_vectors)
]
ranked = sorted(scores, key=lambda x: x[1], reverse=True)


def precision_recall_f1(retrieved_ids, relevant_ids):
    retrieved_set = set(retrieved_ids)
    tp = len(retrieved_set & relevant_ids)
    fp = len(retrieved_set - relevant_ids)
    fn = len(relevant_ids - retrieved_set)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        (2 * precision * recall / (precision + recall))
        if (precision + recall) > 0
        else 0.0
    )
    return precision, recall, f1


if __name__ == "__main__":
    print("Ranking (DocID, CosineSimilarity):")
    for d, s in ranked:
        print(d, round(s, 4))
    for k in range(1, len(docs) + 1):
        topk = [doc_id for doc_id, _ in ranked[:k]]
        P, R, F1 = precision_recall_f1(topk, relevant_set)
        print(f"@{k} -> P={P:.4f} R={R:.4f} F1={F1:.4f}")
