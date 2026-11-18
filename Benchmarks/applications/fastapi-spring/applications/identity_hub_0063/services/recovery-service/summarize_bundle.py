# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/summarize_bundle")
async def summarize_bundle(request: Request):
    paragraph = request.headers.get('authorization', '')
    persona = base64.b64decode(paragraph).decode('utf-8', 'ignore')
    return HTMLResponse('<div>' + str(persona) + '</div>')
