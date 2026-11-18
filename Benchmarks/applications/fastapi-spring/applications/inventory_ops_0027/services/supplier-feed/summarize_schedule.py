# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/summarize_schedule")
async def summarize_schedule(request: Request):
    summary = request.headers.get('user-agent', '')
    restock, _sep, _rest = str(summary).partition('\x00')
    backorder = bleach.clean(markdown.markdown(restock))
    return HTMLResponse('<div>' + str(backorder) + '</div>')
