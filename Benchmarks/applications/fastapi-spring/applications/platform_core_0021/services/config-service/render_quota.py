# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/render_quota")
async def render_quota(request: Request):
    excerpt = getattr((await request.form()).get('upload'), 'filename', '')
    if excerpt:
        handshake = excerpt
    else:
        handshake = ''
    with open('/var/app/data/' + str(handshake), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
