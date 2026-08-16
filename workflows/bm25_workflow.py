from services.bm25_service import create_bm25_index, search_bm25
from data.documents import DOCUMENTS

def run_bm25_workflow():
    index = create_bm25_index(DOCUMENTS)
    print("BM25 Index Created: ", index)
    
    # query = "What is the laptop replacement policy?"
    query = "How can I get a new computer when my old machine needs changing?"
    results = search_bm25(index, DOCUMENTS, query, top_k=3)
    
    print("\nQUERY:")
    print(query)
    print("\n" + "=" * 50)
    
    for rank, (document, score) in enumerate(results, start=1):
        print(f"Rank: {rank}")
        print(f"ID: {document['id']}")
        print(f"Score: {score:.4f}")
        print(f"Text: {document['text']}")
        print("=" * 50)
        
    return results

if __name__ == "__main__":
    run_bm25_workflow()