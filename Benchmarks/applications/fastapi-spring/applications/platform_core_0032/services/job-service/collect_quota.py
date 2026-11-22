# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/collect_quota")
async def collect_quota(request: Request):
    remark = request.cookies.get('session_token', '')
    persona, _sep, _rest = str(remark).partition('\x00')
    handshake = bleach.clean(persona)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(handshake))
    return HTMLResponse(page)
