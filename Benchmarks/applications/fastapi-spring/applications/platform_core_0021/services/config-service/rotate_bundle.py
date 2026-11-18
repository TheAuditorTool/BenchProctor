# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/rotate_bundle")
async def rotate_bundle(request: Request):
    excerpt = request.headers.get('authorization', '')
    parts = []
    for token in str(excerpt).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    subprocess.run(['echo', handshake], shell=False)
    return {"updated": True}
