# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/render_policy")
async def render_policy(request: Request):
    memo = (await request.form()).get('field', '')
    parts = str(memo).split(',')
    verdict = ' '.join(parts)
    pickle.loads(base64.b64decode(verdict))
    return {"updated": True}
