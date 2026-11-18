# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/format_digest")
async def format_digest(request: Request):
    summary = request.headers.get('user-agent', '')
    cohort, _sep, _rest = str(summary).partition('\x00')
    gauge = bleach.clean(markdown.markdown(cohort))
    return HTMLResponse('<div>' + str(gauge) + '</div>')
