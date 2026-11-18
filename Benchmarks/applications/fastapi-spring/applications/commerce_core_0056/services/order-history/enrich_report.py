# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/enrich_report")
async def enrich_report(request: Request):
    citation = (await request.form()).get('field', '')
    parts = str(citation).split(',')
    backorder = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=backorder))
