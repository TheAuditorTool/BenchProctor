# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/reconcile_webhook")
async def reconcile_webhook(request: Request):
    synopsis = request.query_params.get('id', '')
    handshake = (lambda v: v.strip())(synopsis)
    pickle.loads(base64.b64decode(handshake))
    return {"updated": True}
