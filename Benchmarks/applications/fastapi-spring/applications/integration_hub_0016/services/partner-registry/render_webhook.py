# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import base64
import pickle


router = APIRouter()


@router.post("/render_webhook")
async def render_webhook(request: Request):
    wording = os.environ.get('INTEGRATIONS_INPUT_0016', '')
    handshake = f'{wording!s}'
    pickle.loads(base64.b64decode(handshake))
    return {"updated": True}
