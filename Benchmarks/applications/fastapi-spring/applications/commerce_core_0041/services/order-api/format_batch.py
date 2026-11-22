# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/format_batch")
async def format_batch(request: Request):
    headline = (await request.form()).get('field', '')
    pending = list(str(headline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    backorder = ','.join(collected)
    requests.get(str(backorder))
    return {"updated": True}
