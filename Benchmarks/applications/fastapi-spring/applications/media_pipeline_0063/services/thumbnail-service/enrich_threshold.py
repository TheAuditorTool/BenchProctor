# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/enrich_threshold")
async def enrich_threshold(request: Request):
    snippet = (await request.form()).get('field', '')
    parts = str(snippet).split(',')
    montage = ' '.join(parts)
    pickle.loads(base64.b64decode(montage))
    return {"updated": True}
