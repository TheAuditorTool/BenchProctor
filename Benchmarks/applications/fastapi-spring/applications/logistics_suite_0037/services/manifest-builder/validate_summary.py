# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/validate_summary")
async def validate_summary(request: Request):
    footnote = request.cookies.get('session_token', '')
    consignment = footnote if footnote else 'default'
    return HTMLResponse('<div>' + str(consignment) + '</div>')
