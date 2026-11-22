# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/verify_batch")
async def verify_batch(request: Request):
    remark = (await request.form()).get('field', '')
    parts = str(remark).split(',')
    persona = ' '.join(parts)
    pickle.loads(base64.b64decode(persona))
    return {"updated": True}
