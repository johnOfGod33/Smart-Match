from typing import List

from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings_data(text: str | List[str]):
    embedded_data = model.encode(text)

    return embedded_data.tolist()


def get_similarity_score(text1: str, text2: str):
    """text1_embeddings = get_embeddings_data(text1)
    text2_embeddings = get_embeddings_data(text2)"""

    return model.similarity(text1, text2)
