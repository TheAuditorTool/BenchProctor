# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket
import urllib.parse


router = APIRouter()


@router.post("/normalize_receipt")
async def normalize_receipt(request: Request):
    citation = request.headers.get('authorization', '')
    kind = 'json' if str(citation).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            rendition = str(citation).strip()
        case _:
            rendition = str(citation)
    s = socket.create_connection((urllib.parse.urlparse(str(rendition)).hostname, 80))
    s.close()
    return {"updated": True}
