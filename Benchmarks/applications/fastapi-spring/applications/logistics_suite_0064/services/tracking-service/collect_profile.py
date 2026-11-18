# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/collect_profile")
async def collect_profile(request: Request):
    transcript = request.headers.get('authorization', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    subprocess.run(['echo', parcel], shell=False)
    return {"updated": True}
