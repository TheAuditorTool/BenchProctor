# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/compact_index")
async def compact_index(request: Request):
    phrase = request.headers.get('x-custom-header', '')
    dossier = '%s' % (phrase,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(dossier))
    return HTMLResponse(page)
