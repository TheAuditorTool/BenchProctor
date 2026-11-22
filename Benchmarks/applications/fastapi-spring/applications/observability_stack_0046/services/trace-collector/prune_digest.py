# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request


router = APIRouter()


@router.post("/prune_digest")
async def prune_digest(request: Request):
    paragraph = request.headers.get('authorization', '')
    gauge = f'{paragraph!s}'
    outbound = urllib.request.Request(str(gauge), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
