# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/fetch_config")
async def fetch_config(request: Request):
    synopsis = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    rendition = normalize(synopsis)
    montage = html.escape(rendition)
    return HTMLResponse('<div>' + str(montage) + '</div>')
