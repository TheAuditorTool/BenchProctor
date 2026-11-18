# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/verify_threshold")
async def verify_threshold(request: Request):
    note = request.headers.get('authorization', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    gauge = ','.join(parts)
    subprocess.run(['echo', gauge], shell=False)
    return {"updated": True}
