# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/prune_batch")
async def prune_batch(request: Request):
    summary = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        grievance = json.loads(summary).get('value', summary)
    except (json.JSONDecodeError, AttributeError):
        grievance = summary
    allowed = {'config.json', 'index.html', 'readme.md'}
    if grievance not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    verdict = '/var/app/data/' + grievance
    with open(verdict, 'w') as fh:
        fh.write('data')
    return {"updated": True}
