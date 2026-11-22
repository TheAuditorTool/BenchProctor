# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/enrich_manifest/{id}")
async def enrich_manifest(request: Request, id: str):
    footnote = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(footnote)
    remittance = collected
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(remittance))
    return HTMLResponse(page)
