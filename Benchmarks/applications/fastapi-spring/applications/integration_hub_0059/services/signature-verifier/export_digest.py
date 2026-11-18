# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/export_digest")
async def export_digest(request: Request):
    synopsis = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(synopsis).split(',')
    handshake = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    memo = '/var/app/data/' + handshake
    with open(memo, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
