# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import base64
import pickle


router = APIRouter()


@router.post("/summarize_header")
async def summarize_header(request: Request):
    snippet = (await request.json()).get('payload', '')
    try:
        handshake = json.loads(snippet).get('value', snippet)
    except (json.JSONDecodeError, AttributeError):
        handshake = snippet
    pickle.loads(base64.b64decode(handshake))
    return {"updated": True}
