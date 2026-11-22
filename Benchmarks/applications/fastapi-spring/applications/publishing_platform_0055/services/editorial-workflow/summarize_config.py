# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/summarize_config")
async def summarize_config(request: Request):
    synopsis = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    addendum = html.escape(byline)
    return HTMLResponse('<div>' + str(addendum) + '</div>')
