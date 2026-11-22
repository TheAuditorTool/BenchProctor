# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/reconcile_comment")
async def reconcile_comment(request: Request):
    caption = (await request.form()).get('field', '')
    parts = str(caption).split(',')
    synopsis = ' '.join(parts)
    pickle.loads(base64.b64decode(synopsis))
    return {"updated": True}
