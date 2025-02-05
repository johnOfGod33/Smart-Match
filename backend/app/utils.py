from typing import List

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings_data(text: str | List[str]):
    embedded_data = model.encode(text)

    return embedded_data.tolist()
