# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/summarize_schedule")
async def summarize_schedule(request: Request):
    summary = (await request.form()).get('field', '')
    parts = str(summary).split(',')
    bulletin = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=bulletin))
