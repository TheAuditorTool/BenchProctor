# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/summarize_config")
async def summarize_config(request: Request):
    subject = request.headers.get('origin', '')
    pending = list(str(subject).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    grievance = ','.join(collected)
    requests.get(str(grievance))
    return {"updated": True}
