from rank_bm25 import BM25Okapi

def create_bm25_index(documents):
    tokenized_documents = []

    for document in documents:
        # split() returns a list of tokens directly
        text = document["text"].lower().split()
        tokenized_documents.append(text)

    print("Tokenized Documents:\n")
    print(tokenized_documents)

    bm25Index = BM25Okapi(tokenized_documents)
    
    return bm25Index

def search_bm25(index, documents, query, top_k=3):
    # 1. Tokenize query
    query_tokens = query.lower().split()
    
    # 2. Compute BM25 relevance scores for all documents
    scores = index.get_scores(query_tokens)
    
    # 3. Pair documents with their corresponding scores
    document_score_pairs = list(zip(documents, scores))
    
    # 4. Sort documents by score descending
    sorted_pairs = sorted(
        document_score_pairs,
        key=lambda item: item[1],
        reverse=True
    )
    
    # 5. Return top_k matches
    return sorted_pairs[:top_k]

