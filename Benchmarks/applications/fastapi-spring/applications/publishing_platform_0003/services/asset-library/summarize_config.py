# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/summarize_config")
async def summarize_config(request: Request):
    heading = request.cookies.get('session_token', '')
    addendum, _sep, _rest = str(heading).partition('\x00')
    byline = bleach.clean(addendum)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(byline))
    return HTMLResponse(page)
