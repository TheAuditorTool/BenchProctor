# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/rotate_bundle")
async def rotate_bundle(request: Request):
    caption = request.headers.get('origin', '')
    pending = list(str(caption).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    cohort = ','.join(collected)
    requests.get(str(cohort))
    return {"updated": True}
