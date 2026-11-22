# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/archive_receipt/{id}")
async def archive_receipt(request: Request, id: str):
    note = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(note)
    cohort = collected
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(cohort))
    return HTMLResponse(page)
