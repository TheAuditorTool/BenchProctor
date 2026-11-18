# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/settle_capture")
async def settle_capture(request: Request):
    caption = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ledger = RequestPayload(caption).value
    requests.post("http://payments-api:8080/AuthorizePayment", json={"payments_payload": str(ledger)})
    return {"updated": True}
