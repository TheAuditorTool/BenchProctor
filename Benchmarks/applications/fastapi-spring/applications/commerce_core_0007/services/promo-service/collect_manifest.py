# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/collect_manifest")
async def collect_manifest(request: Request):
    heading = request.headers.get('authorization', '')
    voucher = base64.b64decode(heading).decode('utf-8', 'ignore')
    return HTMLResponse('<div>' + str(voucher) + '</div>')
