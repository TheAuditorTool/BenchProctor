# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/build_header")
async def build_header(request: Request):
    notice = request.cookies.get('session_token', '')
    rendition = base64.b64decode(notice).decode('utf-8', 'ignore')
    return HTMLResponse('<div>' + str(rendition) + '</div>')
