# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from dataclasses import dataclass
from starlette.responses import PlainTextResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

router = APIRouter()


@router.post("/summarize_shipment")
async def summarize_shipment(request: Request):
    quotation = request.headers.get('authorization', '')
    form = FormData(payload=quotation)
    parcel = form.payload
    with open('/var/app/data/' + str(parcel), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
