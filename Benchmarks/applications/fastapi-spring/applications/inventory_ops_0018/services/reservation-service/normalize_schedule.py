# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/normalize_schedule")
async def normalize_schedule(request: Request):
    transcript = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        backorder = json.loads(transcript).get('value', transcript)
    except (json.JSONDecodeError, AttributeError):
        backorder = transcript
    allowed = {'config.json', 'index.html', 'readme.md'}
    if backorder not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    restock = '/var/app/data/' + backorder
    with open(restock, 'w') as fh:
        fh.write('data')
    return {"updated": True}
