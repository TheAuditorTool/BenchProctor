# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/archive_receipt")
async def archive_receipt(request: Request):
    excerpt = request.cookies.get('session_token', '')
    verdict, _sep, _rest = str(excerpt).partition('\x00')
    grievance = bleach.clean(verdict)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(grievance))
    return HTMLResponse(page)
