# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/compact_threshold")
async def compact_threshold(request: Request):
    transcript = request.headers.get('x-forwarded-for', '')
    parcel, _sep, _rest = str(transcript).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", parcel):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    consignment = parcel
    return HTMLResponse('<div>' + str(consignment) + '</div>')
