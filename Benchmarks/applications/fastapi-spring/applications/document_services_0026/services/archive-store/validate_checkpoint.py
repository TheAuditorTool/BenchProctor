# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/validate_checkpoint")
async def validate_checkpoint(request: Request):
    preface = request.headers.get('x-custom-header', '')
    addendum = bytes.fromhex(preface).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(addendum))
    return HTMLResponse(page)
