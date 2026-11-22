# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/load_schedule")
async def load_schedule(request: Request):
    wording = request.cookies.get('session_token', '')
    handshake, _sep, _rest = str(wording).partition('\x00')
    subject = bleach.clean(handshake)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(subject))
    return HTMLResponse(page)
