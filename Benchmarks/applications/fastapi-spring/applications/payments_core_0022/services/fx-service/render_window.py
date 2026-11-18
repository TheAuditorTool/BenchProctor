# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/render_window")
async def render_window(request: Request):
    subject = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        ledger = json.loads(subject).get('value', subject)
    except (json.JSONDecodeError, AttributeError):
        ledger = subject
    allowed = {'config.json', 'index.html', 'readme.md'}
    if ledger not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    disbursement = '/var/app/data/' + ledger
    with open(disbursement, 'w') as fh:
        fh.write('data')
    return {"updated": True}
