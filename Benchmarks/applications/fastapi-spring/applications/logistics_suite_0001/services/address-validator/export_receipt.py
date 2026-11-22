# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/export_receipt")
async def export_receipt(request: Request):
    quotation = (await request.body()).decode('utf-8')
    parcel = quotation.decode('utf-8', 'ignore') if isinstance(quotation, bytes) else quotation
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    consignment = parcel
    return HTMLResponse('<div>' + str(consignment) + '</div>')
