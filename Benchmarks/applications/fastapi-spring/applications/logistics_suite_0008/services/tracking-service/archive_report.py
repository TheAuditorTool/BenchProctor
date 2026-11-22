# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse


router = APIRouter()


@router.post("/archive_report")
async def archive_report(request: Request):
    caption = request.headers.get('referer', '')
    consignment = caption if caption else 'default'
    return StreamingResponse(iter(['<div>' + str(consignment) + '</div>']), media_type='text/html')
