# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/collect_record")
async def collect_record(request: Request):
    summary = request.cookies.get('session_token', '')
    restock = summary if summary else 'default'
    return HTMLResponse('<div>' + str(restock) + '</div>')
