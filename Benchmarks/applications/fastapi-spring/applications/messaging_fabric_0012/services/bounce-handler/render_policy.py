# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket
import urllib.parse


router = APIRouter()


@router.post("/render_policy")
async def render_policy(request: Request):
    preface = request.headers.get('authorization', '')
    kind = 'json' if str(preface).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            bulletin = str(preface).strip()
        case _:
            bulletin = str(preface)
    s = socket.create_connection((urllib.parse.urlparse(str(bulletin)).hostname, 80))
    s.close()
    return {"updated": True}
