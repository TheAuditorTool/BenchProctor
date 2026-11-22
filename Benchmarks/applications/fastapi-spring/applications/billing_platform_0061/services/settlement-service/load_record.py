# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from dataclasses import dataclass
from starlette.responses import PlainTextResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

router = APIRouter()


@router.post("/load_record")
async def load_record(request: Request):
    footnote = request.headers.get('authorization', '')
    form = FormData(payload=footnote)
    remittance = form.payload
    with open('/var/app/data/' + str(remittance), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
