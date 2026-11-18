# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/export_window")
async def export_window(request: Request):
    caption = (await request.form()).get('field', '')
    parts = str(caption).split(',')
    cohort = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=cohort))
