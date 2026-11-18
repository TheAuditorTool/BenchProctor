# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/fetch_threshold")
async def fetch_threshold(request: Request):
    headline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(headline).split(',')
    cohort = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if cohort not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    gauge = '/var/app/data/' + cohort
    with open(gauge, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
