# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/prune_checkpoint")
async def prune_checkpoint(request: Request):
    wording = request.query_params.get('id', '')
    handshake = '%s' % (wording,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(handshake))
    return HTMLResponse(page)
