# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/annotate_roster")
async def annotate_roster(request: Request):
    footnote = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(footnote)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, consignment))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    parcel = full_path
    with open(parcel, 'w') as fh:
        fh.write('data')
    return {"updated": True}
