# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/merge_snapshot")
async def merge_snapshot(request: Request):
    note = request.headers.get('authorization', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    subprocess.run(['echo', handshake], shell=False)
    return {"updated": True}
