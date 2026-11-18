# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/prune_record")
async def prune_record(request: Request):
    remark = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, remittance))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    arrears = full_path
    with open(arrears, 'w') as fh:
        fh.write('data')
    return {"updated": True}
