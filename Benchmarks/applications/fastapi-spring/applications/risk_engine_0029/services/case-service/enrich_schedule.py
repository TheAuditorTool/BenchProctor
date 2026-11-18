# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/enrich_schedule")
async def enrich_schedule(request: Request):
    subject = request.headers.get('user-agent', '')
    grievance, _sep, _rest = str(subject).partition('\x00')
    verdict = bleach.clean(markdown.markdown(grievance))
    return HTMLResponse('<div>' + str(verdict) + '</div>')
