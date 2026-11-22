# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/normalize_config")
async def normalize_config(request: Request):
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    phrase = normalize(summary)
    subtitle = html.escape(phrase)
    return HTMLResponse('<div>' + str(subtitle) + '</div>')
