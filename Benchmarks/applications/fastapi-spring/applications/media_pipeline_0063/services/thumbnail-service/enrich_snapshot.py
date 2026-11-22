# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/enrich_snapshot")
async def enrich_snapshot(request: Request):
    snippet = request.cookies.get('session_token', '')
    montage, _sep, _rest = str(snippet).partition('\x00')
    rendition = bleach.clean(montage)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(rendition))
    return HTMLResponse(page)
