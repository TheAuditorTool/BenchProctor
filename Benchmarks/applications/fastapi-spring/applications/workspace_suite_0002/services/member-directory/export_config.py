# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/export_config")
async def export_config(request: Request):
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(transcript).split(',')
    heading = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if heading not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    passage = '/var/app/data/' + heading
    with open(passage, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
