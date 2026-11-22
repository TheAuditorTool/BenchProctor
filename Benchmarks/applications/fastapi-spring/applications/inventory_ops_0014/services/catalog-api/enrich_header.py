# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request


router = APIRouter()


@router.post("/enrich_header")
async def enrich_header(request: Request):
    excerpt = request.headers.get('authorization', '')
    restock = f'{excerpt!s}'
    outbound = urllib.request.Request(str(restock), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
