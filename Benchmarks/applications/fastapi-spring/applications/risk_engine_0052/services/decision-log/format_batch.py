# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/format_batch")
async def format_batch(request: Request):
    memo = request.headers.get('x-custom-header', '')
    verdict = '%s' % (memo,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(verdict))
    return HTMLResponse(page)
