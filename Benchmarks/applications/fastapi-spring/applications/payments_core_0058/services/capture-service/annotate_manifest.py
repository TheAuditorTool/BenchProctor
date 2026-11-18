# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/annotate_manifest")
async def annotate_manifest(request: Request):
    caption = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        ledger = json.loads(caption).get('value', caption)
    except (json.JSONDecodeError, AttributeError):
        ledger = caption
    allowed = {'config.json', 'index.html', 'readme.md'}
    if ledger not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    remittance = '/var/app/data/' + ledger
    with open(remittance, 'w') as fh:
        fh.write('data')
    return {"updated": True}
