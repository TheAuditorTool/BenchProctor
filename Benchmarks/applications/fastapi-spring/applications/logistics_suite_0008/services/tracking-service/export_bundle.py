# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/export_bundle")
async def export_bundle(request: Request):
    caption = (await request.body()).decode('utf-8')
    consignment = caption.decode('utf-8', 'ignore') if isinstance(caption, bytes) else caption
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    return HTMLResponse('<div>' + str(parcel) + '</div>')
