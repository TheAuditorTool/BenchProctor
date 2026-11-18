# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/compact_checkpoint")
async def compact_checkpoint(request: Request):
    citation = request.headers.get('authorization', '')
    backorder = base64.b64decode(citation).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    restock = backorder
    os.system('echo ' + str(restock))
    return {"updated": True}
