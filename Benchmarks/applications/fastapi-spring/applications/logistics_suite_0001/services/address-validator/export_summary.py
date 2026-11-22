# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/export_summary")
async def export_summary(request: Request):
    quotation = request.cookies.get('session_token', '')
    parcel, _sep, _rest = str(quotation).partition('\x00')
    consignment = bleach.clean(parcel)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(consignment))
    return HTMLResponse(page)
