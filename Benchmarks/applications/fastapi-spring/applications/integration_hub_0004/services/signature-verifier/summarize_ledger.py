# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/summarize_ledger/{id}")
async def summarize_ledger(request: Request, id: str):
    summary = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(summary)
    handshake = collected
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(handshake))
    return HTMLResponse(page)
