# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/fetch_header")
async def fetch_header(request: Request):
    summary = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(summary)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, addendum))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    byline = full_path
    with open(byline, 'w') as fh:
        fh.write('data')
    return {"updated": True}
