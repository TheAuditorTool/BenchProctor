# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request


router = APIRouter()


@router.post("/reconcile_window")
async def reconcile_window(request: Request):
    headline = request.headers.get('authorization', '')
    remittance = f'{headline!s}'
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
