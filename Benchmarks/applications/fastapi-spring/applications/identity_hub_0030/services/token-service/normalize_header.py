# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/normalize_header")
async def normalize_header(request: Request):
    tagline = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    persona = normalize(tagline)
    note = html.escape(persona)
    return HTMLResponse('<div>' + str(note) + '</div>')
