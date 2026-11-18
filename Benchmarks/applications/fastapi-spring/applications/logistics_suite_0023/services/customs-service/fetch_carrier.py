# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/fetch_carrier")
async def fetch_carrier(request: Request):
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(caption).split(',')
    parcel = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if parcel not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    consignment = '/var/app/data/' + parcel
    with open(consignment, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
