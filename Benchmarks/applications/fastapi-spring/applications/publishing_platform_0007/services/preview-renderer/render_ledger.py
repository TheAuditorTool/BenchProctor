# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/render_ledger")
async def render_ledger(request: Request):
    remark = request.headers.get('x-custom-header', '')
    byline = '%s' % (remark,)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(byline))
    return HTMLResponse(page)
