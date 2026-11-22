# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/build_payout")
async def build_payout(request: Request):
    footnote = (await request.form()).get('field', '')
    remittance = (lambda v: v.strip())(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    disbursement = remittance
    subprocess.run('echo ' + str(disbursement), shell=True)
    return {"updated": True}
