# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/prune_profile")
async def prune_profile(request: Request):
    remark = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        remittance = json.loads(remark).get('value', remark)
    except (json.JSONDecodeError, AttributeError):
        remittance = remark
    allowed = {'config.json', 'index.html', 'readme.md'}
    if remittance not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    arrears = '/var/app/data/' + remittance
    with open(arrears, 'w') as fh:
        fh.write('data')
    return {"updated": True}
