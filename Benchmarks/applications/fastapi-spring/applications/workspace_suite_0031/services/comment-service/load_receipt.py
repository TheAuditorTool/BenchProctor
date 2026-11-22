# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/load_receipt")
async def load_receipt(request: Request):
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    synopsis = normalize(caption)
    snippet = html.escape(synopsis)
    return HTMLResponse('<div>' + str(snippet) + '</div>')
