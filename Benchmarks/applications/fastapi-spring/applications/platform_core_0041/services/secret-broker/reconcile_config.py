# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/reconcile_config")
async def reconcile_config(request: Request):
    passage = request.headers.get('user-agent', '')
    persona, _sep, _rest = str(passage).partition('\x00')
    handshake = bleach.clean(markdown.markdown(persona))
    return HTMLResponse('<div>' + str(handshake) + '</div>')
