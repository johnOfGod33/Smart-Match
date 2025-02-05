from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI

from .. import utils
from ..configs import settings

router = APIRouter(prefix="/embeddings")


@router.get("/", status_code=201)
async def calculate_similarity(text_to_encode: str, text_to_search: str):
    try:
        embedded_data = utils.get_embeddings(text_to_encode)
        embedded_to_compare = utils.get_embeddings(text_to_search)

        return utils.calculate_similarity(embedded_data, embedded_to_compare).tolist()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
