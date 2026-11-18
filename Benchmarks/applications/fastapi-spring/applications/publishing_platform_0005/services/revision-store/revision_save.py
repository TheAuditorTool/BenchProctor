# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/save_revision")
async def save_revision(request: Request):
    footnote = request.headers.get('origin', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            byline = str(footnote).strip()
        case _:
            byline = str(footnote)
    requests.post("http://preview-renderer:8080/RenderPreview", json={"publishing_payload": str(byline)})
    return {"updated": True}
