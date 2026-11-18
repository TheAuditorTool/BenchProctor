# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/prune_roster")
async def prune_roster(request: Request):
    footnote = (await request.form()).get('field', '')
    parts = str(footnote).split(',')
    byline = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=byline))
