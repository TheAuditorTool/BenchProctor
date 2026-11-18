# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/reconcile_schedule")
async def reconcile_schedule(request: Request):
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(transcript).split(',')
    backorder = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if backorder not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    restock = '/var/app/data/' + backorder
    with open(restock, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
