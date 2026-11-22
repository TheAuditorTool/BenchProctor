# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/summarize_config")
async def summarize_config(request: Request):
    phrase = request.cookies.get('session_token', '')
    grievance, _sep, _rest = str(phrase).partition('\x00')
    inquiry = bleach.clean(grievance)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(inquiry))
    return HTMLResponse(page)
