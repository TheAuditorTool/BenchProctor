# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/resolve_batch")
async def resolve_batch(request: Request):
    summary = (await request.form()).get('field', '')
    parts = str(summary).split(',')
    addendum = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=addendum))
