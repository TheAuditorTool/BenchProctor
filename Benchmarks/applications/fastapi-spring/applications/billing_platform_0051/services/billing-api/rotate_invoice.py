# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import base64
import pickle


router = APIRouter()


@router.post("/rotate_invoice")
async def rotate_invoice(request: Request):
    synopsis = (await request.json()).get('payload', '')
    try:
        arrears = json.loads(synopsis).get('value', synopsis)
    except (json.JSONDecodeError, AttributeError):
        arrears = synopsis
    pickle.loads(base64.b64decode(arrears))
    return {"updated": True}
