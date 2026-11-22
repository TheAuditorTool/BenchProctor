# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/render_roster")
async def render_roster(request: Request):
    transcript = (await request.body()).decode('utf-8')
    pending = list(str(transcript).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    consignment = ','.join(collected)
    requests.get(str(consignment))
    return {"updated": True}
