# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/summarize_webhook")
async def summarize_webhook(request: Request):
    snippet = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        handshake = json.loads(snippet).get('value', snippet)
    except (json.JSONDecodeError, AttributeError):
        handshake = snippet
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    paragraph = '/var/app/data/' + handshake
    with open(paragraph, 'w') as fh:
        fh.write('data')
    return {"updated": True}
