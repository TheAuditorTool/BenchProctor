# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_bundle")
async def verify_bundle(request: Request):
    transcript = (await request.body()).decode('utf-8')
    consignment = transcript.decode('utf-8', 'ignore') if isinstance(transcript, bytes) else transcript
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    return HTMLResponse('<div>' + str(parcel) + '</div>')
