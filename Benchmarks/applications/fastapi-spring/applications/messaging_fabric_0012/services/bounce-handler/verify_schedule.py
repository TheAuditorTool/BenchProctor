# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/verify_schedule")
async def verify_schedule(request: Request):
    preface = request.headers.get('x-custom-header', '')
    bulletin = '%s' % (preface,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(bulletin))
    return HTMLResponse(page)
