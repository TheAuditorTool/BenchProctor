# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from app_runtime import db


router = APIRouter()


@router.post("/merge_report")
async def merge_report(request: Request):
    subtitle = db.fetch_one('SELECT name FROM users LIMIT 1')
    if subtitle:
        persona = subtitle
    else:
        persona = ''
    return HTMLResponse('<div>' + str(persona) + '</div>')
