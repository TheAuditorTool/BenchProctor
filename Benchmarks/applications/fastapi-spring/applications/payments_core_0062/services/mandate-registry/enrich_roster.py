# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


request_state: dict[str, str] = {}

router = APIRouter()


@router.post("/enrich_roster/{id}")
async def enrich_roster(request: Request, id: str):
    headline = request.path_params.get('id', '')
    request_state['last_input'] = headline
    disbursement = request_state['last_input']
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(disbursement))
    return HTMLResponse(page)
