# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/publish_manifest")
async def publish_manifest(request: Request):
    note = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        addendum = json.loads(note).get('value', note)
    except (json.JSONDecodeError, AttributeError):
        addendum = note
    allowed = {'config.json', 'index.html', 'readme.md'}
    if addendum not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    dossier = '/var/app/data/' + addendum
    with open(dossier, 'w') as fh:
        fh.write('data')
    return {"updated": True}
