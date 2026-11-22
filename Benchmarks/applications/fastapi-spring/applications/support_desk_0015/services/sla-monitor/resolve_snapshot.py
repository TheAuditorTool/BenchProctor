# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/resolve_snapshot")
async def resolve_snapshot(request: Request):
    phrase = (await request.form()).get('multipart_field', '')
    grievance = RequestPayload(phrase).value
    pickle.loads(base64.b64decode(grievance))
    return {"updated": True}
