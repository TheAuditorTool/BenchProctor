# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/verify_policy")
async def verify_policy(request: Request):
    phrase = request.cookies.get('session_token', '')
    dossier, _sep, _rest = str(phrase).partition('\x00')
    addendum = bleach.clean(dossier)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(addendum))
    return HTMLResponse(page)
