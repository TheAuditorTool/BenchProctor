# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/rotate_summary")
async def rotate_summary(request: Request):
    snippet = request.query_params.get('id', '')
    persona = (lambda v: v.strip())(snippet)
    pickle.loads(base64.b64decode(persona))
    return {"updated": True}
