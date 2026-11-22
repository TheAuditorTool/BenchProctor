# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/build_macro")
async def build_macro(request: Request):
    blurb = (await request.form()).get('field', '')
    parts = str(blurb).split(',')
    inquiry = ' '.join(parts)
    pickle.loads(base64.b64decode(inquiry))
    return {"updated": True}
