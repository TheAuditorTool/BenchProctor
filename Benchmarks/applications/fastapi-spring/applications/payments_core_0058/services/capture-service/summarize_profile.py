# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/summarize_profile")
async def summarize_profile(request: Request):
    caption = request.headers.get('user-agent', '')
    ledger, _sep, _rest = str(caption).partition('\x00')
    remittance = bleach.clean(markdown.markdown(ledger))
    return HTMLResponse('<div>' + str(remittance) + '</div>')
