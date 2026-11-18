# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/render_summary")
async def render_summary(request: Request):
    transcript = request.headers.get('authorization', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    heading = ','.join(parts)
    subprocess.run(['echo', heading], shell=False)
    return {"updated": True}
