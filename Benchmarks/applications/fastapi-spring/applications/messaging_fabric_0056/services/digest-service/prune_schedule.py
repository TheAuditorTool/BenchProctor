# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/prune_schedule")
async def prune_schedule(request: Request):
    footnote = request.cookies.get('session_token', '')
    bulletin, _sep, _rest = str(footnote).partition('\x00')
    snippet = bleach.clean(bulletin)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(snippet))
    return HTMLResponse(page)
