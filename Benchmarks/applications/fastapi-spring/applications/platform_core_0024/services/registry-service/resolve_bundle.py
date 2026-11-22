# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/resolve_bundle")
async def resolve_bundle(request: Request):
    heading = request.cookies.get('session_token', '')
    handshake, _sep, _rest = str(heading).partition('\x00')
    persona = bleach.clean(handshake)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(persona))
    return HTMLResponse(page)
