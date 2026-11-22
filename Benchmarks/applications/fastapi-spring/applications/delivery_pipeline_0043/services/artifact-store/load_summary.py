# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse


router = APIRouter()


@router.post("/load_summary")
async def load_summary(request: Request):
    remark = request.headers.get('referer', '')
    note = remark if remark else 'default'
    return StreamingResponse(iter(['<div>' + str(note) + '</div>']), media_type='text/html')
