# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/rotate_snapshot")
async def rotate_snapshot(request: Request):
    footnote = request.cookies.get('session_token', '')
    byline = footnote if footnote else 'default'
    return HTMLResponse('<div>' + str(byline) + '</div>')
