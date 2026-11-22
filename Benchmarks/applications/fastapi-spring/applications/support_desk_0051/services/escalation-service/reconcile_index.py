# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_index")
async def reconcile_index(request: Request):
    preface = (await request.form()).get('field', '')
    grievance = (lambda v: v.strip())(preface)
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return {"updated": True}
