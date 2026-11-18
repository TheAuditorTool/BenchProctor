# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/audit_header")
async def audit_header(request: Request):
    summary = request.headers.get('origin', '')
    kind = 'json' if str(summary).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            restock = str(summary).strip()
        case _:
            restock = str(summary)
    requests.get(str(restock))
    return {"updated": True}
