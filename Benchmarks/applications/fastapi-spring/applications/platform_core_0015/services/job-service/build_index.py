# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/build_index")
async def build_index(request: Request):
    note = (await request.form()).get('field', '')
    parts = str(note).split(',')
    handshake = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=handshake))
