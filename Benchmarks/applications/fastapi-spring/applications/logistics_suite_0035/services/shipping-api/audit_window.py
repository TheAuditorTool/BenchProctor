# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/audit_window")
async def audit_window(request: Request):
    phrase = getattr((await request.form()).get('upload'), 'filename', '')
    if phrase:
        parcel = phrase
    else:
        parcel = ''
    with open('/var/app/data/' + str(parcel), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
