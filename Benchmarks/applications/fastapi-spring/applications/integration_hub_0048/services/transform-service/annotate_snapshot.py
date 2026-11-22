# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from dataclasses import dataclass
from starlette.responses import PlainTextResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

router = APIRouter()


@router.post("/annotate_snapshot")
async def annotate_snapshot(request: Request):
    citation = request.headers.get('authorization', '')
    form = FormData(payload=citation)
    handshake = form.payload
    with open('/var/app/data/' + str(handshake), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
