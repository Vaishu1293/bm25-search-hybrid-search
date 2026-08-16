from services.bm25_service import create_bm25_index
from data.documents import DOCUMENTS

def run_bm25_workflow():
    index = create_bm25_index(DOCUMENTS)
    print("BM25 Index Created: ", index)
    return