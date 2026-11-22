# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse


router = APIRouter()


@router.post("/validate_alert")
async def validate_alert(request: Request):
    excerpt = request.headers.get('referer', '')
    cohort = excerpt if excerpt else 'default'
    return StreamingResponse(iter(['<div>' + str(cohort) + '</div>']), media_type='text/html')
