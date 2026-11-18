# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/load_policy")
async def load_policy(request: Request):
    memo = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    return HTMLResponse('<div>' + str(voucher) + '</div>')
