# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/prune_window")
async def prune_window(request: Request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    note = normalize(remark)
    phrase = html.escape(note)
    return HTMLResponse('<div>' + str(phrase) + '</div>')
