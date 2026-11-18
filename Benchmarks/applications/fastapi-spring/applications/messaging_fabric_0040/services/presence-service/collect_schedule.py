# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/collect_schedule")
async def collect_schedule(request: Request):
    preface = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(preface).split(',')
    bulletin = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if bulletin not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    notice = '/var/app/data/' + bulletin
    with open(notice, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
