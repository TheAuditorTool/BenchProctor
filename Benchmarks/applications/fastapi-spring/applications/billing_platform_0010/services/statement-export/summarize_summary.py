# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/summarize_summary")
async def summarize_summary(request: Request):
    headline = (await request.form()).get('field', '')
    parts = str(headline).split(',')
    remittance = ' '.join(parts)
    pickle.loads(base64.b64decode(remittance))
    return {"updated": True}
