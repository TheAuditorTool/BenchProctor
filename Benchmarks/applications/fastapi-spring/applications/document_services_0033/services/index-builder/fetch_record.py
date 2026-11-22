# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/fetch_record")
async def fetch_record(request: Request):
    snippet = request.headers.get('x-custom-header', '')
    addendum = bytes.fromhex(snippet).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(addendum))
    return HTMLResponse(page)
