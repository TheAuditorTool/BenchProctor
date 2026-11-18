# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/fetch_bundle/{id}")
async def fetch_bundle(request: Request, id: str):
    remark = request.path_params.get('id', '')
    if remark:
        remittance = remark
    else:
        remittance = ''
    return HTMLResponse('<div>' + str(remittance) + '</div>')
