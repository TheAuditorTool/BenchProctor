# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import bleach
from starlette.responses import HTMLResponse
from jinja2 import Environment


router = APIRouter()


@router.post("/normalize_receipt")
async def normalize_receipt(request: Request):
    wording = request.cookies.get('session_token', '')
    backorder, _sep, _rest = str(wording).partition('\x00')
    voucher = bleach.clean(backorder)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(voucher))
    return HTMLResponse(page)
