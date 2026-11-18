# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/verify_config")
async def verify_config(request: Request):
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(footnote).split(',')
    handshake = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    blurb = '/var/app/data/' + handshake
    with open(blurb, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
