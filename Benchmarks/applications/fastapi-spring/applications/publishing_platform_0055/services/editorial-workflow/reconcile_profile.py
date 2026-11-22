# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/reconcile_profile")
async def reconcile_profile(request: Request):
    synopsis = request.query_params.get('id', '')
    byline = '%s' % (synopsis,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(byline))
    return HTMLResponse(page)
