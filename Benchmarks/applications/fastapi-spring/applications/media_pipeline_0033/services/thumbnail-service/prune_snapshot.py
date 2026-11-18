# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/prune_snapshot")
async def prune_snapshot(request: Request):
    transcript = request.headers.get('authorization', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    subprocess.run(['echo', rendition], shell=False)
    return {"updated": True}
