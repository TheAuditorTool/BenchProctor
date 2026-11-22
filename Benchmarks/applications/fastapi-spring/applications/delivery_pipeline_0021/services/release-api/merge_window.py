# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/merge_window")
async def merge_window(request: Request):
    summary = (await request.form()).get('field', '')
    pending = list(str(summary).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    phrase = ','.join(collected)
    requests.get(str(phrase))
    return {"updated": True}
