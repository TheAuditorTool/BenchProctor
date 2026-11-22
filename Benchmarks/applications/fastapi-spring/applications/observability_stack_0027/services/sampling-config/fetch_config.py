# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket
import urllib.parse


router = APIRouter()


@router.post("/fetch_config")
async def fetch_config(request: Request):
    remark = request.headers.get('authorization', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            gauge = str(remark).strip()
        case _:
            gauge = str(remark)
    s = socket.create_connection((urllib.parse.urlparse(str(gauge)).hostname, 80))
    s.close()
    return {"updated": True}
