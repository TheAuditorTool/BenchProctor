# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from dataclasses import dataclass
from starlette.responses import PlainTextResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

router = APIRouter()


@router.post("/merge_receipt")
async def merge_receipt(request: Request):
    transcript = request.headers.get('authorization', '')
    form = FormData(payload=transcript)
    addendum = form.payload
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
