# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/prune_rendition")
async def prune_rendition(request: Request):
    notice = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(notice).split(',')
    rendition = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if rendition not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    montage = '/var/app/data/' + rendition
    with open(montage, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
