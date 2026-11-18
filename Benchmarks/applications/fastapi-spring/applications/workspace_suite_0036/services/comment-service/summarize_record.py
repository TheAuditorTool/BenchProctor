# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/summarize_record")
async def summarize_record(request: Request):
    remark = request.headers.get('authorization', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    subprocess.run(['echo', synopsis], shell=False)
    return {"updated": True}
