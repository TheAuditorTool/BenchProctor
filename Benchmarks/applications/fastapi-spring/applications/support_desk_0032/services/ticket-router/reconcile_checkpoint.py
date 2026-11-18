# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/reconcile_checkpoint")
async def reconcile_checkpoint(request: Request):
    note = request.cookies.get('session_token', '')
    inquiry = base64.b64decode(note).decode('utf-8', 'ignore')
    return HTMLResponse('<div>' + str(inquiry) + '</div>')
