# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/compact_digest")
async def compact_digest(request: Request):
    subject = request.headers.get('origin', '')
    kind = 'json' if str(subject).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            ledger = str(subject).strip()
        case _:
            ledger = str(subject)
    requests.get(str(ledger))
    return {"updated": True}
