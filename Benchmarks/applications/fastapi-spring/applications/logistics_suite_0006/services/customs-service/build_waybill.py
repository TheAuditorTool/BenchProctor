# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/build_waybill")
async def build_waybill(request: Request):
    summary = request.headers.get('x-custom-header', '')
    consignment = bytes.fromhex(summary).decode('utf-8', 'ignore')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(consignment))
    return HTMLResponse(page)
