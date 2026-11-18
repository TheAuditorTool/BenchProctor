# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/compact_roster")
async def compact_roster(request: Request):
    synopsis = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, byline))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = full_path
    with open(addendum, 'w') as fh:
        fh.write('data')
    return {"updated": True}
