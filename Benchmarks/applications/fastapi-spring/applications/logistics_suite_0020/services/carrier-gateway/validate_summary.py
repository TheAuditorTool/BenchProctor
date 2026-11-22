# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_summary")
async def validate_summary(request: Request):
    transcript = (await request.form()).get('field', '')
    consignment, _sep, _rest = str(transcript).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    subprocess.run('echo ' + str(parcel), shell=True)
    return {"updated": True}
