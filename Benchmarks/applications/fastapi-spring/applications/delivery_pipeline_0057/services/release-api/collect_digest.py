# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/collect_digest")
async def collect_digest(request: Request):
    footnote = request.headers.get('authorization', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    wording = ','.join(parts)
    subprocess.run(['echo', wording], shell=False)
    return {"updated": True}
