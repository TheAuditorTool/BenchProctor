# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/resolve_window")
async def resolve_window(request: Request):
    caption = request.headers.get('authorization', '')
    gauge = (lambda v: v.strip())(caption)
    return HTMLResponse('<div>' + str(gauge) + '</div>')
