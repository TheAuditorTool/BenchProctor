# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_policy")
async def verify_policy(request: Request):
    citation = (await request.form()).get('field', '')
    parcel = (lambda v: v.strip())(citation)
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    consignment = parcel
    subprocess.run('echo ' + str(consignment), shell=True)
    return {"updated": True}
