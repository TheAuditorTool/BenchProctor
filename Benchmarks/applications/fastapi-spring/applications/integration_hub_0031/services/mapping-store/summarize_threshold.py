# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/summarize_threshold")
async def summarize_threshold(request: Request):
    snippet = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(snippet).split(',')
    handshake = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    paragraph = '/var/app/data/' + handshake
    with open(paragraph, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
