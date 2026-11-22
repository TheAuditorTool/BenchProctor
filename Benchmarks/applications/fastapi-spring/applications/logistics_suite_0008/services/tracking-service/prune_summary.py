# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/prune_summary")
async def prune_summary(request: Request):
    caption = request.headers.get('x-custom-header', '')
    consignment = bytes.fromhex(caption).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(consignment))
    return HTMLResponse(page)
