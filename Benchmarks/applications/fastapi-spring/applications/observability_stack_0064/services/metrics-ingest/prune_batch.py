# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/prune_batch")
async def prune_batch(request: Request):
    tagline = request.headers.get('x-custom-header', '')
    gauge = '%s' % (tagline,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(gauge))
    return HTMLResponse(page)
