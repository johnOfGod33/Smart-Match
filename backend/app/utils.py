from typing import List

<<<<<<< HEAD
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import BinaryClassificationEvaluator
=======
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
>>>>>>> feat/optimize_scoring_with_many_embedding

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings_data(text: str | List[str]):
    embedded_data = model.encode(text)

    return embedded_data.tolist()


def get_similarity_score(text1: str, text2: str):
<<<<<<< HEAD
    embeddings1 = get_embeddings_data(text1)
    embeddings2 = get_embeddings_data(text2)

    print(model.similarity(embeddings1, embeddings2))


def evaluate_embeddings(text1: str, text2: str):
    binary_acc_evaluator = BinaryClassificationEvaluator(
        sentences1=text1, sentences2=text2, name="accuracy"
    )

    results = binary_acc_evaluator(model)

    print(results)
=======
    """text1_embeddings = get_embeddings_data(text1)
    text2_embeddings = get_embeddings_data(text2)"""

    return model.similarity(text1, text2)
>>>>>>> feat/optimize_scoring_with_many_embedding
