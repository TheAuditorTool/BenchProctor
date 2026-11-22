# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse


router = APIRouter()


@router.post("/normalize_checkpoint")
async def normalize_checkpoint(request: Request):
    note = request.headers.get('referer', '')
    byline = note if note else 'default'
    return StreamingResponse(iter(['<div>' + str(byline) + '</div>']), media_type='text/html')
