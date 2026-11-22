# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse


router = APIRouter()


@router.post("/publish_snapshot")
async def publish_snapshot(request: Request):
    heading = request.headers.get('referer', '')
    handshake = heading if heading else 'default'
    return StreamingResponse(iter(['<div>' + str(handshake) + '</div>']), media_type='text/html')
