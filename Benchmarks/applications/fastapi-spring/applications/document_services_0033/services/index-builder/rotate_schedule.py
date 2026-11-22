# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket
import urllib.parse


router = APIRouter()


@router.post("/rotate_schedule")
async def rotate_schedule(request: Request):
    snippet = request.headers.get('authorization', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            addendum = str(snippet).strip()
        case _:
            addendum = str(snippet)
    s = socket.create_connection((urllib.parse.urlparse(str(addendum)).hostname, 80))
    s.close()
    return {"updated": True}
