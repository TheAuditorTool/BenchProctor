# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/summarize_wallet")
async def summarize_wallet(request: Request):
    subject = request.headers.get('user-agent', '')
    ledger, _sep, _rest = str(subject).partition('\x00')
    disbursement = bleach.clean(markdown.markdown(ledger))
    return HTMLResponse('<div>' + str(disbursement) + '</div>')
