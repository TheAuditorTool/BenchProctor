# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/publish_window")
async def publish_window(request: Request):
    heading = (await request.body()).decode('utf-8')
    pending = list(str(heading).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    requests.get(str(handshake))
    return {"updated": True}
