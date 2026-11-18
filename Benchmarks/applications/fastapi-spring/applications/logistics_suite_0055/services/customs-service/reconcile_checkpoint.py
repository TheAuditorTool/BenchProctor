# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/reconcile_checkpoint")
async def reconcile_checkpoint(request: Request):
    heading = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    return HTMLResponse('<div>' + str(consignment) + '</div>')
