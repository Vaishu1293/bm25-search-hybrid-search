"""Environment and application dependency setup."""

import os

# from dotenv import load_dotenv

# from config import PDF_COLLECTION
# from services.chroma_service import create_client, create_collection
# from services.gemini_service import load_genai_client


# def load_api_key() -> str:
#     """Load and return the Gemini API key from the .env file."""
#     load_dotenv()
#     api_key = os.getenv("GEMINI_API_KEY", "")

#     if not api_key:
#         raise ValueError("GEMINI_API_KEY is missing from the environment.")

#     return api_key


# def get_setup_components(collection_name: str = PDF_COLLECTION) -> tuple:
#     """Create the Gemini client, Chroma client, and requested collection."""
#     api_key = load_api_key()
#     client = load_genai_client(api_key)
#     chroma_client = create_client()
#     collection = create_collection(chroma_client, collection_name)

#     return api_key, client, chroma_client, collection
