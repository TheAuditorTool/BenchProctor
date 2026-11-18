# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/annotate_receipt/{id}")
async def annotate_receipt(request: Request, id: str):
    tagline = request.path_params.get('id', '')
    if tagline:
        rendition = tagline
    else:
        rendition = ''
    return HTMLResponse('<div>' + str(rendition) + '</div>')
