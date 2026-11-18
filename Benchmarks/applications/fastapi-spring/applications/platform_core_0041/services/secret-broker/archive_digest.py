# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/archive_digest")
async def archive_digest(request: Request):
    passage = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    persona = normalize(passage)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, persona))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    handshake = full_path
    with open(handshake, 'w') as fh:
        fh.write('data')
    return {"updated": True}
