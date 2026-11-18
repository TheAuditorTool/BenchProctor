# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/build_receipt/{id}")
async def build_receipt(request: Request, id: str):
    snippet = request.path_params.get('id', '')
    if snippet:
        persona = snippet
    else:
        persona = ''
    return HTMLResponse('<div>' + str(persona) + '</div>')
