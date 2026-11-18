# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/merge_record")
async def merge_record(request: Request):
    snippet = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        persona = json.loads(snippet).get('value', snippet)
    except (json.JSONDecodeError, AttributeError):
        persona = snippet
    allowed = {'config.json', 'index.html', 'readme.md'}
    if persona not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    handshake = '/var/app/data/' + persona
    with open(handshake, 'w') as fh:
        fh.write('data')
    return {"updated": True}
