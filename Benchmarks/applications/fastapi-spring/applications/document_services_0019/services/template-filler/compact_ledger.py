# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/compact_ledger")
async def compact_ledger(request: Request):
    passage = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        dossier = json.loads(passage).get('value', passage)
    except (json.JSONDecodeError, AttributeError):
        dossier = passage
    allowed = {'config.json', 'index.html', 'readme.md'}
    if dossier not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = '/var/app/data/' + dossier
    with open(addendum, 'w') as fh:
        fh.write('data')
    return {"updated": True}
