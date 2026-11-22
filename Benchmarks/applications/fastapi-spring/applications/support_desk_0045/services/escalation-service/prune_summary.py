# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/prune_summary")
async def prune_summary(request: Request):
    remark = request.cookies.get('session_token', '')
    inquiry, _sep, _rest = str(remark).partition('\x00')
    grievance = bleach.clean(inquiry)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(grievance))
    return HTMLResponse(page)
