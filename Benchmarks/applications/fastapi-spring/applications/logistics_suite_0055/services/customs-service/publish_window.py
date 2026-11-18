# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import markdown
import bleach


router = APIRouter()


@router.post("/publish_window")
async def publish_window(request: Request):
    heading = request.headers.get('user-agent', '')
    consignment, _sep, _rest = str(heading).partition('\x00')
    parcel = bleach.clean(markdown.markdown(consignment))
    return HTMLResponse('<div>' + str(parcel) + '</div>')
