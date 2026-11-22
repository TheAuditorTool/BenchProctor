# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from app_runtime import db


router = APIRouter()


@router.post("/compact_connector")
async def compact_connector(request: Request):
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    if caption:
        handshake = caption
    else:
        handshake = ''
    return HTMLResponse('<div>' + str(handshake) + '</div>')
