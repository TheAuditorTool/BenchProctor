# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/collect_report")
async def collect_report(request: Request):
    snippet = (await request.form()).get('field', '')
    parts = str(snippet).split(',')
    handshake = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=handshake))
