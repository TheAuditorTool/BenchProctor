# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_summary")
async def prune_summary(request: Request):
    caption = (await request.body()).decode('utf-8')
    remittance = caption.decode('utf-8', 'ignore') if isinstance(caption, bytes) else caption
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = remittance
    return HTMLResponse('<div>' + str(dunning) + '</div>')
