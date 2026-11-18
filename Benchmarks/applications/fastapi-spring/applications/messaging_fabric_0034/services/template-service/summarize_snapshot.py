# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/summarize_snapshot")
async def summarize_snapshot(request: Request):
    footnote = request.headers.get('origin', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            bulletin = str(footnote).strip()
        case _:
            bulletin = str(footnote)
    requests.get(str(bulletin))
    return {"updated": True}
