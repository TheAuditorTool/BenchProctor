# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/export_policy")
async def export_policy(request: Request):
    blurb = request.headers.get('x-custom-header', '')
    inquiry = bytes.fromhex(blurb).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(inquiry))
    return HTMLResponse(page)
