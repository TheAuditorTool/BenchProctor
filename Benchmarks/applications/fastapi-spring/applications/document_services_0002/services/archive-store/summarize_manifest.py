# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


request_state: dict[str, str] = {}

router = APIRouter()


@router.post("/summarize_manifest/{id}")
async def summarize_manifest(request: Request, id: str):
    wording = request.path_params.get('id', '')
    request_state['last_input'] = wording
    addendum = request_state['last_input']
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(addendum))
    return HTMLResponse(page)
