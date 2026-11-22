# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/summarize_policy")
async def summarize_policy(request: Request):
    paragraph = request.headers.get('x-custom-header', '')
    persona = bytes.fromhex(paragraph).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(persona))
    return HTMLResponse(page)
