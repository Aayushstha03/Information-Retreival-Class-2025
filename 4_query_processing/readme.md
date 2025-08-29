# Lab 4: Query Processing in Information Retrieval

This lab demonstrates several key techniques for query processing and spelling correction in information retrieval systems:

## 1. Query Expansion
- **WordNet-based Expansion:**  
  Uses the WordNet lexical database to find synonyms for query terms, expanding the query to include semantically related words. This helps retrieve documents that may use different words with similar meanings.

## 2. Spelling Correction Techniques
- **Edit Distance (Levenshtein Distance):**  
  Finds the closest word in the vocabulary to a misspelled query term by calculating the minimum number of single-character edits required.
- **K-Gram Index:**  
  Builds an index of k-length substrings (k-grams) from vocabulary words. Misspelled words are corrected by finding vocabulary words with the highest k-gram overlap, then selecting the closest by edit distance.
- **Context-Sensitive Correction (Bigram Model):**  
  Uses bigram frequencies from the corpus to choose corrections that fit the context of surrounding words, improving accuracy for multi-word queries.

## 3. Query Language Interpreter
- **Single-Word Query:**  
  Retrieves documents containing the exact query word.
- **Boolean Query:**  
  Supports logical operators (AND, OR, NOT) to combine search terms for more precise document retrieval.
- **Natural Language Query:**  
  Tokenizes plain English queries and matches documents containing any of the query terms.
- **Structural Query:**  
  Allows field-specific searches (e.g., `title:cat`), useful for structured documents.

---

Each technique is implemented with clear code examples and explanations, providing a practical introduction to query processing and spelling correction in IR