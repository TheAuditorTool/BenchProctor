# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/post_comment")
async def post_comment(request: Request):
    caption = request.headers.get('authorization', '')
    kind = 'json' if str(caption).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            synopsis = str(caption).strip()
        case _:
            synopsis = str(caption)
    requests.post("http://share-service:8080/GrantShare", json={"workspace_payload": str(synopsis)})
    return {"updated": True}
