# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/collect_record")
async def collect_record(request: Request):
    synopsis = request.headers.get('authorization', '')
    parts = []
    for token in str(synopsis).split(','):
        parts.append(token.strip())
    verdict = ','.join(parts)
    subprocess.run(['echo', verdict], shell=False)
    return {"updated": True}
