# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request


router = APIRouter()


@router.post("/format_receipt")
async def format_receipt(request: Request):
    subtitle = request.headers.get('authorization', '')
    persona = f'{subtitle!s}'
    outbound = urllib.request.Request(str(persona), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
