# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/audit_roster")
async def audit_roster(request: Request):
    wording = request.headers.get('x-custom-header', '')
    backorder = bytes.fromhex(wording).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(backorder))
    return HTMLResponse(page)
