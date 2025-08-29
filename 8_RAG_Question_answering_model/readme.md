## https://github.com/Aayushstha03/pdf-chat

You can find my previous work of creating a RAG system capable of answering in a conversational fashion to natural language queries, based on a PDF doc that you upload.
The system uses : 
1. Ollama : for models to create embeddings (nomic-embed) and the coversational LLM (Llama3.2)
2. Langchain : for easy orchestration
3. ChromaDB : to store embeddings for the docs, reduce repetition, contains logic to check if a block has already been embedded or not.
4. FireCrawl : a SERP scraping service that allows the LLM to answer queries based on the search results.
