# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_ledger")
async def annotate_ledger(request: Request):
    caption = (await request.form()).get('field', '')
    synopsis = (lambda v: v.strip())(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(synopsis)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    snippet = synopsis
    subprocess.run('echo ' + str(snippet), shell=True)
    return {"updated": True}
