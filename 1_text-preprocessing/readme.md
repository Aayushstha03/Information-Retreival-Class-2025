
# Lab: Text Preprocessing in Information Retrieval

This lab demonstrates essential text preprocessing techniques and statistical analyses for natural language data:

## 1. Data Loading
- Loads datasets (e.g., jokes-partial.csv, riwaj.csv) into pandas DataFrames for processing.

## 2. Initial Text Cleaning
- Lowercases text, removes punctuation, numbers, URLs, and HTML tags (where present).
- Normalizes whitespace.

## 3. Tokenization
- Splits cleaned text into word tokens using NLTK's word_tokenize.

## 4. Stopword Removal
- Removes common English stopwords using NLTK's stopwords list.

## 5. Normalization
- **Stemming:** Uses PorterStemmer to reduce words to their root forms.
- **Lemmatization:** Uses WordNetLemmatizer, with and without POS tagging, to convert words to their base forms.

## 6. Statistical Analysis
- **Zipf's Law:** Plots word frequency vs. rank on a log-log scale and checks the Zipfian relationship for the most frequent words.
- **Heaps' Law:** Plots vocabulary size vs. corpus size to observe sub-linear vocabulary growth.

## 7. Visualization
- **Word Cloud:** Generates a word cloud from lemmatized word frequencies for visual analysis.

---

All steps are implemented with clear code and explanations, providing a practical introduction to text preprocessing and statistical analysis in IR. Where steps are repeated across datasets, the code adapts to the specific data structure (e.g., column names) but the core techniques remain the same.
