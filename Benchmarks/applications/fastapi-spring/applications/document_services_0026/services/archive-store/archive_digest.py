# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/archive_digest/{id}")
async def archive_digest(request: Request, id: str):
    preface = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(preface)
    addendum = collected
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(addendum))
    return HTMLResponse(page)
