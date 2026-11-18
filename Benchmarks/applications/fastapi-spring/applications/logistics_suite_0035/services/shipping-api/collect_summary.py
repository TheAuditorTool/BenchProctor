# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/collect_summary/{id}")
async def collect_summary(request: Request, id: str):
    phrase = request.path_params.get('id', '')
    if phrase:
        parcel = phrase
    else:
        parcel = ''
    return HTMLResponse('<div>' + str(parcel) + '</div>')
