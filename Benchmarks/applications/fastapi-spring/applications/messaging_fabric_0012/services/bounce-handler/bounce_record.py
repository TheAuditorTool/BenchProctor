# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/record_bounce")
async def record_bounce(request: Request):
    preface = (await request.form()).get('multipart_field', '')
    bulletin = RequestPayload(preface).value
    requests.post("http://delivery-service:8080/DispatchDelivery", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
