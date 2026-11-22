# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/annotate_bundle")
async def annotate_bundle(request: Request):
    citation = request.headers.get('x-custom-header', '')
    dossier = '%s' % (citation,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(dossier))
    return HTMLResponse(page)
