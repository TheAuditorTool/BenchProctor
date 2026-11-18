# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/audit_threshold")
async def audit_threshold(request: Request):
    phrase = (await request.form()).get('field', '')
    parts = str(phrase).split(',')
    persona = ' '.join(parts)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=persona))
