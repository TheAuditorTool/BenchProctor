# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_label")
async def prune_label(request: Request):
    footnote = request.cookies.get('session_token', '')
    consignment = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    return HTMLResponse('<div>' + str(parcel) + '</div>')
