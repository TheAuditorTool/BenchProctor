# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/enrich_schedule")
async def enrich_schedule(request: Request):
    synopsis = (await request.form()).get('field', '')
    parts = str(synopsis).split(',')
    rendition = ' '.join(parts)
    pickle.loads(base64.b64decode(rendition))
    return {"updated": True}
