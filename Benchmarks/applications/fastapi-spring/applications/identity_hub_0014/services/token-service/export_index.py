# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/export_index")
async def export_index(request: Request):
    snippet = getattr((await request.form()).get('upload'), 'filename', '')
    if snippet:
        persona = snippet
    else:
        persona = ''
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
