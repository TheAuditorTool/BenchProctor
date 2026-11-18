# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/fetch_summary")
async def fetch_summary(request: Request):
    heading = request.headers.get('authorization', '')
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    subprocess.run(['echo', voucher], shell=False)
    return {"updated": True}
