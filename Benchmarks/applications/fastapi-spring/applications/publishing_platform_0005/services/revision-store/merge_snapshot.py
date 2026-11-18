# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/merge_snapshot")
async def merge_snapshot(request: Request):
    footnote = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    byline = normalize(footnote)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, byline))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = full_path
    with open(addendum, 'w') as fh:
        fh.write('data')
    return {"updated": True}
