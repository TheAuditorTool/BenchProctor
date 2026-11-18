# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/compact_manifest/{id}")
async def compact_manifest(request: Request, id: str):
    note = request.path_params.get('id', '')
    if note:
        gauge = note
    else:
        gauge = ''
    return HTMLResponse('<div>' + str(gauge) + '</div>')
