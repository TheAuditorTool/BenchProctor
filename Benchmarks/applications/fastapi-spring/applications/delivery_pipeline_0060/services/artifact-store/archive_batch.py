# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/archive_batch/{id}")
async def archive_batch(request: Request, id: str):
    wording = request.path_params.get('id', '')
    if wording:
        remark = wording
    else:
        remark = ''
    return HTMLResponse('<div>' + str(remark) + '</div>')
