# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/fetch_threshold")
async def fetch_threshold(request: Request):
    heading = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    addendum = normalize(heading)
    byline = html.escape(addendum)
    return HTMLResponse('<div>' + str(byline) + '</div>')
