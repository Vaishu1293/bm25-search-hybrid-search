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