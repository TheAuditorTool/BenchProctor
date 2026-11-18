# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/fetch_index")
async def fetch_index(request: Request):
    summary = request.headers.get('user-agent', '')
    gauge, _sep, _rest = str(summary).partition('\x00')
    cohort = bleach.clean(markdown.markdown(gauge))
    return HTMLResponse('<div>' + str(cohort) + '</div>')
