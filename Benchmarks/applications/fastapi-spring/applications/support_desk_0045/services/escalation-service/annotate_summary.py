# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/annotate_summary")
async def annotate_summary(request: Request):
    remark = request.cookies.get('session_token', '')
    parts = str(remark).split(',')
    inquiry = ' '.join(parts)
    parsed = json.loads(inquiry)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
