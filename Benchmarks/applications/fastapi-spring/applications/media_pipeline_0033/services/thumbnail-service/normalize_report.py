# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/normalize_report")
async def normalize_report(request: Request):
    transcript = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(transcript)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, rendition))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    montage = full_path
    with open(montage, 'w') as fh:
        fh.write('data')
    return {"updated": True}
