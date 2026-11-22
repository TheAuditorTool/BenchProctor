# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/audit_manifest")
async def audit_manifest(request: Request):
    remark = request.query_params.get('id', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    return HTMLResponse('<div>' + str(inquiry) + '</div>')
