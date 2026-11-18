# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/format_header")
async def format_header(request: Request):
    transcript = request.headers.get('origin', '')
    pending = list(str(transcript).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    backorder = ','.join(collected)
    requests.get(str(backorder))
    return {"updated": True}
