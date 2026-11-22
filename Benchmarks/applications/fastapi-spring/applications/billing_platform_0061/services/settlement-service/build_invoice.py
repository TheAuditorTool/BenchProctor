# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/build_invoice")
async def build_invoice(request: Request):
    footnote = request.cookies.get('session_token', '')
    remittance, _sep, _rest = str(footnote).partition('\x00')
    arrears = bleach.clean(remittance)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(arrears))
    return HTMLResponse(page)
