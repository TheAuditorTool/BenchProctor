# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/verify_schedule")
async def verify_schedule(request: Request):
    notice = getattr((await request.form()).get('upload'), 'filename', '')
    if notice:
        persona = notice
    else:
        persona = ''
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
