# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/merge_manifest")
async def merge_manifest(request: Request):
    snippet = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(snippet).split(',')
    persona = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if persona not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    synopsis = '/var/app/data/' + persona
    with open(synopsis, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
