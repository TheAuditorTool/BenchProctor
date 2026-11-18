# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/build_batch/{id}")
async def build_batch(request: Request, id: str):
    note = request.path_params.get('id', '')
    if note:
        handshake = note
    else:
        handshake = ''
    return HTMLResponse('<div>' + str(handshake) + '</div>')
